class MusicPlayer(object):  # 创建一个音乐播放器

    def __new__(cls, *args, **kwargs):
        print("创建对象，分配空间")  # 1. 创建对象时，new方法会被自动调
        instance = super().__new__(cls)  # 2. 为对象分配空间
        return instance  # 3. 返回对象的引用，必须的有这个返回，不然self找不到对象

    def __init__(self,name):  # 初始化方法；对这个实例化对象再次加工<br>　　　　　
        self.name = name
        self._n="cde"
        print("播放器初始化")

    def run(self):
        print(self._n)
        print(self.name)

if __name__=="__main__":
    player = MusicPlayer("小米")
    player.run()