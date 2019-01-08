# coding: utf-8

from scene import *

from PIL import Image
import ui, io
''' urlから読み込む際は以下を追加 '''
#from requests import get

class MyScene(Scene):
	def setup(self):
		''' 画像をPILimageとして読み込む '''
		pil_img = Image.open('test:Lenna')
		''' urlから読み込むときの書き方 '''
		#url = 'https://'
		#pil_img = Image.open(io.BytesIO(get(url).content))

		# PILimageをUIimageに変換する
		with io.BytesIO() as f:
			pil_img.save(f, format='png')
			ui_img = ui.Image.from_data(f.getvalue())
		
		# sceneで扱う為、UIimageをTextureに変換する
		texture = Texture(ui_img)

		# SpriteNodeを使い、スクリーンに追加する
		self.img = SpriteNode(texture, position=self.size/2)
		self.add_child(self.img)

if __name__=='__main__':
	run(MyScene(), show_fps=False)