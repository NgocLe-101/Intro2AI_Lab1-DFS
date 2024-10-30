# Ares's Adventure

## Phân tích bài toán

Với trạng thái ban đầu của input, yêu cầu của ta là tìm chuỗi hành động của Ares để đến được trạng thái cuối cùng là tất cả các viên đá đều nằm trên các switch. Mặt khác, với mỗi vị trí của Ares trên mê cung, anh ta có tối đa 4 khả năng để đi tiếp ở bước tiếp theo. \
![alt text](/assets/image.png) \
Như vậy, bài toán được quy về bài toán tìm kiếm với không gian trạng thái là trạng thái của mê cung sau mỗi bước di chuyển của Ares. Trạng thái ban đầu chính là trạng thái của input và trạng thái kết thúc chính là lúc các viên đá đều nằm trên các switch. Hàm successor sẽ tìm ra các khả năng hành động của Ares ở trạng thái hiện tại với cost dựa trên hành động đó \
![alt text](/assets/image-1.png)

## Thuật toán DFS

Với việc bài toán được quy về bài toán tìm kiếm, các thuật toán tìm kiếm có thể được sử dụng để tìm lời giải cho bài toán này, trong đó có DFS. \
Với node là trạng thái của mê cung, khi một node được xét, ta sẽ tìm các node lân cận của node vừa tìm được (các trạng thái tiếp theo của mê cung khi Ares đi từ node hiện tại) và cho vào tập mở. Sau đó, ta xét node sau cùng được thêm vào và cho nó vào tập đóng (FIFO). Cứ như vậy, bài toán giải được khi trạng thái đích của mê cung đạt được (đến đích) hoặc stack rỗng (không còn trạng thái nào để đi).

## Cách xây dựng

Trạng thái của mê cung được lưu dưới dạng là một Object Maze nhận vào thông tin của mê cung như vị trí người chơi (Ares), vị trí của các viên đá, vị trí của các switch, vị trí của các bức tường. Đây cũng là node để xét và thêm vào tập mở ở mỗi bước

```python
class Maze:
    def __init__(mazeState : MazeState):
        ...
```

Tại mỗi node được xét, ta sẽ thêm các node lân cận (các trạng thái của mê cung có thể đạt được khi Ares di chuyển tại node hiện tại)

```python
availableMoves = currentMaze.getPlayerMoves()
for move in availableMoves:
    newMaze = currentMaze.copy()
    moveCost = newMaze.onPlayerMove(move) # update maze on move
    if newMaze not in traveled:
        stack.append((newMaze, path + [move], cost + moveCost))
```

Khi stack vẫn còn phần tử, ta xét node mới nhất ở trong stack

```python
while stack:
    ...
    currentMaze, path, cost = stack.pop()
```

Khi đạt được trạng thái kết thúc (nghĩa là các viên đá đều ở trên switch), kết thúc thuật toán

```python
if currentMaze.isEnded():
    ...
    print(path, cost)
    ...
    File.exportSolutionToFile(fileInfo['caseIndex'], 'DFS', len(pathStr), pathStr, cost, nodesGenerated, searchTime, memoryUsed)
    return
```

## Một số tối ưu & ràng buộc cho thuật toán

### Ràng buộc về độ sâu tìm kiếm

```python
MAX_DEPTH = 1e6 # Avoid traversing too long
if depth > MAX_DEPTH:
    ...
    print('Exceed max depth')
    return
```

### Cache các vị trí có thể đi được của Ares trên mê cung

```python
global availablePosition
availablePosition = MazeHelper.getAvailablePosition(mazeMatrix) # Cache available position to reduce time complexity and space complexity
...
def __availablePosition(self, location):
    return location in availablePosition
```
