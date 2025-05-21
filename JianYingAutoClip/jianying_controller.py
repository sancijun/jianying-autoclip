"""剪映自动化控制，这是跨平台替代版本"""

import warnings
from enum import Enum
from typing import Optional, Literal

class Export_resolution(Enum):
    """导出分辨率"""
    RES_8K = "8K"
    RES_4K = "4K"
    RES_2K = "2K"
    RES_1080P = "1080P"
    RES_720P = "720P"
    RES_480P = "480P"

class Export_framerate(Enum):
    """导出帧率"""
    FR_24 = "24fps"
    FR_25 = "25fps"
    FR_30 = "30fps"
    FR_50 = "50fps"
    FR_60 = "60fps"

class Jianying_controller:
    """
    剪映控制器 - 跨平台替代版本
    
    注意：此版本仅提供接口兼容性，不包含实际功能。
    自动控制功能仅在 Windows 平台下可用。
    """

    app_status: Literal["home", "edit", "pre_export"]

    def __init__(self):
        """初始化剪映控制器（仅兼容接口，无实际功能）"""
        warnings.warn(
            "自动控制功能仅在 Windows 平台下可用。此版本仅提供接口兼容性，无实际功能。",
            RuntimeWarning, stacklevel=2
        )
        self.app_status = "home"

    def export_draft(self, draft_name: str, output_path: Optional[str] = None, *,
                     resolution: Optional[Export_resolution] = None,
                     framerate: Optional[Export_framerate] = None,
                     timeout: float = 1200) -> None:
        """
        导出指定的剪映草稿（仅兼容接口，无实际功能）
        
        此功能仅在 Windows 平台下可用。
        """
        warnings.warn(
            "自动导出功能仅在 Windows 平台下可用。此版本仅提供接口兼容性，无实际功能。",
            RuntimeWarning, stacklevel=2
        )
        print(f"[模拟] 导出 {draft_name} 至 {output_path} (此功能仅在 Windows 平台下可用)")

    def switch_to_home(self) -> None:
        """
        切换到剪映主页（仅兼容接口，无实际功能）
        
        此功能仅在 Windows 平台下可用。
        """
        warnings.warn(
            "自动控制功能仅在 Windows 平台下可用。此版本仅提供接口兼容性，无实际功能。",
            RuntimeWarning, stacklevel=2
        )

    def get_window(self) -> None:
        """
        寻找剪映窗口并置顶（仅兼容接口，无实际功能）
        
        此功能仅在 Windows 平台下可用。
        """
        warnings.warn(
            "自动控制功能仅在 Windows 平台下可用。此版本仅提供接口兼容性，无实际功能。",
            RuntimeWarning, stacklevel=2
        )
