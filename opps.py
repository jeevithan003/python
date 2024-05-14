class m():
    def __init__(self) -> None:
        print("A")
class n(m):
    def __init__(self) -> None:
        super().__init__()
        print("B")
class o(n,m):
    def __init__(self) -> None:
        super().__init__()
        print("C")
onb=o()