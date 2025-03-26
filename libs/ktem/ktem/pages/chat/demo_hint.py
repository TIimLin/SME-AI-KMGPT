from textwrap import dedent

import gradio as gr
from ktem.app import BasePage


class HintPage(BasePage):
    def __init__(self, app):
        self._app = app
        self.on_building_ui()

    def on_building_ui(self):
        with gr.Accordion(label="提示", open=False):
            gr.Markdown(
                dedent(
                    """
                - 您可以從聊天回答中選擇任何文字來**突出顯示相關引用**在右側面板。
                - **引用**可以在 PDF 查看器和原始文本中查看。
                - 您可以在**聊天設置**菜單中調整引用格式並使用高級（CoT）推理。
                - 想要**探索更多**？查看**幫助**部分以創建您的私人空間。
            """  # noqa
                )
            )
