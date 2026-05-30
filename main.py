import os
import sys
import webview


def resource(rel_path):
    base = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base, rel_path)


if __name__ == '__main__':
    html = resource('c.html').replace('\\', '/')
    webview.create_window(
        '超市计算器',
        f'file:///{html}',
        width=460,
        height=780,
        resizable=True,
        min_size=(380, 620),
    )
    webview.start()
