from setuptools import setup, find_packages

setup(
    name="JianYingAutoClip",
    version="0.0.1",
    author="sancijun",
    description="轻量、灵活、易上手的Python剪映草稿生成及导出工具，构建全自动化视频剪辑/混剪流水线",
    long_description=open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/sancijun/jianying-autoclip.git",
    packages=find_packages(),
    package_data={
        'JianYingAutoClip': ['draft_content_template.json']
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Development Status :: 4 - Beta",
        "Topic :: Multimedia :: Video"
    ],
    python_requires='>=3.8',
    install_requires=[
        "pymediainfo",
        "imageio"
    ],
)
