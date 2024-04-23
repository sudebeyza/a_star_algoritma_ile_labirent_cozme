# Python'da bir Yıldız Algoritması Görselleştirme uygulaması

# Gerekli kitaplıkları içe aktarma
import pygame
import math
from queue import PriorityQueue


# Renkler modülünden tüm renkleri içe aktarma
from colors import *

# Küresel Değişkenler

# Pygame penceresinin genişliği
WIDTH = 800


# Pygame penceresinin Genişlik ve Yüksekliğini ayarlama
WIN = pygame.display.set_mode((WIDTH, WIDTH))


# Pygame penceresinin başlığını ayarlama
pygame.display.set_caption("A Star ile Labirent Cozme")

# Class Node
class Node:
    def __init__(self, row, col, width, totalRows):
        self.row = row
        self.col = col
        self.width = width
        self.totalRows = totalRows

        self.x = row * width
        self.y = col * width

        self.color = WHITE

        self.neighbors = []

    
# Pygame penceresinde düğümün konumunu döndüren yöntem
    def getPosition(self):
        return self.row, self.col

    # Düğümün açık olup olmadığını kontrol eden yöntem
    def isOpen(self):
        return self.color == GREEN

    
# Düğümün kapalı olup olmadığını kontrol eden yöntem
    def isClosed(self):
        return self.color == RED

    # Düğümün bir engel olup olmadığını kontrol eden yöntem
    def isBarrier(self):
        return self.color == BLACK

    # Düğümün başlangıç ​​düğümü olup olmadığını kontrol eden yöntem
    def isStart(self):
        return self.color == ORANGE

    
    # Düğümün bitiş düğümü olup olmadığını kontrol eden yöntem
    def isEnd(self):
        return self.color == TURQUOISE

    
    # Düğümü sıfırlayan yöntem
    def reset(self):
        self.color = WHITE

    
    # Düğümü açan yöntem
    def makeOpen(self):
        self.color = GREEN

    
    # Düğümü kapatan yöntem
    def makeClosed(self):
        self.color = RED

    
    # Düğümü bir bariyer yapan yöntem
    def makeBarrier(self):
        self.color = BLACK
    
    # Düğümü başlangıç ​​düğümü yapan yöntem
    def makeStart(self):
        self.color = ORANGE

    
    # Düğümü bitiş düğümü yapan yöntem
    def makeEnd(self):
        self.color = TURQUOISE

    # Düğümü kaynaktan hedef düğüme giden yolun bir parçası yapan yöntem
    def makePath(self):
        self.color = PURPLE

    # Düğümü pygame penceresine çeken yöntem
    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.width))

    # Düğümün komşularını güncelleyen yöntem
    def updateNeighbors(self, grid):
        self.neighbors = []
        
        # Kuzey Komşu
        if self.row > 0 and not grid[self.row - 1][self.col].isBarrier():
            self.neighbors.append(grid[self.row - 1][self.col])

        # Güney Komşu
        if self.row < self.totalRows - 1 and not grid[self.row + 1][self.col].isBarrier():
            self.neighbors.append(grid[self.row + 1][self.col])

        # Doğu Komşusu
        if self.col < self.totalRows - 1 and not grid[self.row][self.col + 1].isBarrier():
            self.neighbors.append(grid[self.row][self.col + 1])

        # Batı Komşusu
        if self.col > 0 and not grid[self.row][self.col - 1].isBarrier():
            self.neighbors.append(grid[self.row][self.col - 1])


    def __lt__(self, other):
        return False

# Kaynaktan hedef düğüme giden yolu çizen fonksiyon
def drawPath(predecessor, currentNode, draw):
    while currentNode in predecessor:
        currentNode = predecessor[currentNode]
        currentNode.makePath()
        draw()

# Bir Yıldız Algoritması Fonksiyonu
def AStarAlgorithm(draw, grid, startNode, endNode):
    count = 0

    # OpenSet bir öncelik sırasıdır
    openSet = PriorityQueue()
    openSet.put((0, count, startNode))

    predecessor = {}

    # Global Score (gScore)
    gScore = {node: float("inf") for row in grid for node in row}
    gScore[startNode] = 0

    # Heuristic Score (fScore)
    fScore = {node: float("inf") for row in grid for node in row}
    fScore[startNode] = heuristicFunction(startNode.getPosition(), endNode.getPosition())

    openSetHash = {startNode}

    while not openSet.empty():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        current = openSet.get()[2]
        openSetHash.remove(current)

        if current == endNode:
            drawPath(predecessor, endNode, draw)
            endNode.makeEnd()
            print(f"The End Node is {temp_gScore} units away from the Source Node")
            return True

        for neighbor in current.neighbors:
            temp_gScore = gScore[current] + 1

            if temp_gScore < gScore[neighbor]:
                predecessor[neighbor] = current
                gScore[neighbor] = temp_gScore
                fScore[neighbor] = temp_gScore + heuristicFunction(neighbor.getPosition(), endNode.getPosition())
                if neighbor not in openSetHash:
                    count += 1
                    openSet.put((fScore[neighbor], count, neighbor))
                    openSetHash.add(neighbor)
                    neighbor.makeOpen()

        draw()

        if current != startNode:
            current.makeClosed()

    return False

#  Heuristic değeri hesaplama işlevi
def heuristicFunction(d1, d2):
    x1, y1 = d1
    x2, y2 = d2
    
    return abs(x1 - x2) + abs(y1 - y2)

# Düğüm ızgarası yapan fonksiyon
def makeGrid(rows, width):
    grid = []
    gap = width // rows

    for i in range(rows):
        grid.append([])

        for j in range(rows):
            node = Node(i, j, gap, rows)
            grid[i].append(node)

    return grid

# Izgaradaki düğümlerin sınırını çizme fonksiyonu
def drawGrid(win, rows, width):
    gap = width // rows

    for i in range(rows):
        pygame.draw.line(win, GREY, (0, i * gap), (width, i * gap))

        for j in range(rows):
            pygame.draw.line(win, GREY, (j * gap, 0), (j * gap, width))

# Pygame penceresindeki ızgaradan düğümleri çizen fonksiyon
def draw(win, grid, rows, width):
    win.fill(WHITE)

    for row in grid:
        for node in row:
            node.draw(win)

    drawGrid(win, rows, width)
    pygame.display.update()

# Pygame penceresinde fare konumunu alan fonksiyon
def getMouseClickPosition(position, rows, width):
    gap = width // rows
    y, x = position

    row = y // gap
    col = x // gap

    return row, col


def main(win, width):

    ROWS = 50  # Satır sayısı

    grid = makeGrid(ROWS, width)
    
    # Başlangıç ​​ve bitiş düğümünü başlatma
    startNode = None
    endNode = None

    run = True

    while run:

        # Izgarayı pygame penceresine çizme
        draw(win, grid, ROWS, width)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            # Sol Fare Düğmesine tıklama kontrolü
            if pygame.mouse.get_pressed()[0]:
                position = pygame.mouse.get_pos()
                row, col = getMouseClickPosition(position, ROWS, width)
                node = grid[row][col]

                # Başlangıç ​​düğümü ayarlanmamışsa,
                # Tıklanan düğümü başlangıç ​​düğümü olarak ayarladık
                if not startNode and node != endNode:
                    startNode = node
                    startNode.makeStart()

                # Uç düğüm ayarlanmamışsa,
                # tıklanmakta olan düğümü bitiş düğümü olarak ayarladık
                elif not endNode and node != startNode:
                    endNode = node
                    endNode.makeEnd()

                # Bariyer düğümü ayarlanmamışsa,
                # Tıklanan düğümü bariyer düğümü olarak ayarladık
                elif node != startNode and node != endNode:
                    node.makeBarrier()                
            
            # Sağ Fare Düğmesine tıklama kontrolü
            elif pygame.mouse.get_pressed()[2]:
                position = pygame.mouse.get_pos()
                row, col = getMouseClickPosition(position, ROWS, width)
                node = grid[row][col]
                node.reset()

                if node == startNode:
                    startNode = None
                elif node == endNode:
                    endNode = None

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and startNode and endNode:
                    for row in grid:
                        for node in row:
                            node.updateNeighbors(grid)

                    AStarAlgorithm(lambda: draw(win, grid, ROWS, width), grid, startNode, endNode)

                if event.key == pygame.K_c:
                    startNode = None
                    endNode = None
                    grid = makeGrid(ROWS, width)

    pygame.quit()

# Ana döngü
if __name__ == "__main__":
    main(WIN, WIDTH)