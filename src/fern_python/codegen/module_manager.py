import os
from collections import defaultdict
from dataclasses import dataclass
from typing import DefaultDict, Set, Tuple

from . import AST
from .filepath import ExportStrategy, Filepath
from .writer_impl import WriterImpl

RelativeModulePath = Tuple[str, ...]


@dataclass
class ModuleInfo:
    exports: DefaultDict[RelativeModulePath, Set[str]]


def create_empty_module_info() -> ModuleInfo:
    return ModuleInfo(exports=defaultdict(set))


class ModuleManager:
    """
    A utility for managing the __init__.py files in a project
    """

    _module_infos: DefaultDict[AST.ModulePath, ModuleInfo]

    def __init__(self, *, should_format: bool) -> None:
        self._module_infos = defaultdict(create_empty_module_info)
        self._should_format = should_format

    def register_exports(self, filepath: Filepath, exports: Set[str]) -> None:
        module_being_exported_from: AST.ModulePath = tuple(
            directory.module_name for directory in filepath.directories
        ) + (filepath.file.module_name,)

        is_exporting_from_file = True

        while len(module_being_exported_from) > 0:
            relative_module_being_exported_from = module_being_exported_from[-1:]
            exporting_module = module_being_exported_from[:-1]
            module_info = self._module_infos[exporting_module]
            export_strategy = (
                ExportStrategy(export_all=True)
                if is_exporting_from_file
                else filepath.directories[len(module_being_exported_from) - 1].export_strategy
            )

            # this shouldn't happen but is necessary to appease mypy
            if export_strategy is None:
                break

            new_exports = set()
            if export_strategy.export_all:
                new_exports.update(exports)
                module_info.exports[relative_module_being_exported_from].update(exports)
            if export_strategy.export_as_namespace:
                namespace_export = set(relative_module_being_exported_from)
                module_info.exports[()].update(namespace_export)
                new_exports.update(namespace_export)
            exports = new_exports

            module_being_exported_from = exporting_module
            is_exporting_from_file = False

    def write_modules(self, filepath: str) -> None:
        for module, module_info in self._module_infos.items():
            with WriterImpl(
                filepath=os.path.join(filepath, *module, "__init__.py"), should_format=self._should_format
            ) as writer:
                all_exports: Set[str] = set()
                for exported_from, exports in module_info.exports.items():
                    if len(exports) > 0:
                        writer.write_line(f"from .{'.'.join(exported_from)} import {', '.join(exports)}")
                        all_exports.update(exports)
                if len(all_exports) > 0:
                    writer.write_line("__all__ = [" + ", ".join(f'"{export}"' for export in sorted(all_exports)) + "]")
