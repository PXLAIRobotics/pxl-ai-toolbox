import pygame
from operator import attrgetter
from graph import Graph, Node

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
GREEN = (0,180,0)
YELLOW = (200,150,0)
NODE_SIZE = 8

def main():
    pygame.init()
    
    pygame.display.set_caption("Graph Visual")
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

    graph = loadGraph('meta.data')    
    graph.status()

    drawGraph(graph, screen)
     
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

# Loads graph from given file
# Rewrite this function if another file format needs to be read
def loadGraph(file):
    graph = Graph()
    with open(file) as fp:
        for l in fp:
            line = l.strip()
            if len(line) > 0 and not line[0] == "#":
                split = line.split(";")
                if split[0] == "NODE":
                    graph.addNode(split[1], Node(split[1], split[2], split[3]))
                elif split[0] == "EDGE":
                    graph.addEdge(split[1], split[2])
    return graph

# Use lat & lon values to draw nodes on canvas (min & max mapped to canvas size)
def drawGraph(graph, screen):
    min_x = min(graph.nodeArray, key=attrgetter('x')).x
    max_x = max(graph.nodeArray, key=attrgetter('x')).x

    min_y = min(graph.nodeArray, key=attrgetter('y')).y
    max_y = max(graph.nodeArray, key=attrgetter('y')).y

    draw_width = SCREEN_WIDTH*0.8
    draw_height = SCREEN_HEIGHT*0.8
    
    start_x = SCREEN_WIDTH*0.1
    start_y = SCREEN_HEIGHT*0.1

    factor = draw_width / (max_x - min_x)

    # Draw nodes
    for node in graph.nodeArray:
        x = start_x + ((node.x - min_x) * factor)
        y = SCREEN_HEIGHT - (start_y + ((node.y - min_y) * factor))
        node.draw_pos = (x, y)
        pygame.draw.rect(screen, GREEN, [x-NODE_SIZE/2,y-NODE_SIZE/2,NODE_SIZE,NODE_SIZE])

    # Draw edges
    for node in graph.nodeArray:
        for neighbour in node.costs:
            target_node = graph.nodes[neighbour]
            pygame.draw.line(screen, YELLOW, node.draw_pos, target_node.draw_pos)

    pygame.display.update()
     
if __name__=="__main__":
    main()