/*
 * 邻接表表示的图的拓扑排序
 */

#include <stdio.h>
#include <stdlib.h>


typedef enum {false, true} bool;
#define MaxVertexNum 10  /* maximum number of vertices */
typedef int Vertex;      /* vertices are numbered from 0 to MaxVertexNum-1 */

typedef struct AdjVNode *PtrToAdjVNode;

// 一条边
struct AdjVNode{
    Vertex AdjV;
    PtrToAdjVNode Next;
};

// 邻接表
typedef struct Vnode{
    PtrToAdjVNode FirstEdge;  /* 邻接表中顶点的第一条边 */
} AdjList[MaxVertexNum];


typedef struct GNode *PtrToGNode;
struct GNode{
    int Nv;  // 顶点个数
    int Ne;  // 边的个数
    AdjList G;  // 所有的顶点
};
typedef PtrToGNode LGraph;

LGraph ReadG(); /* details omitted */

bool TopSort( LGraph Graph, Vertex TopOrder[] );

int main()
{
    int i;
    Vertex TopOrder[MaxVertexNum];
    LGraph G = ReadG();

    if ( TopSort(G, TopOrder)==true )
        for ( i=0; i<G->Nv; i++ )
            printf("%d ", TopOrder[i]);
    else
        printf("ERROR");
    printf("\n");

    return 0;
}


LGraph ReadG()
{
  AdjList adjList;
  PtrToAdjVNode ptrToAdjVNode[MaxVertexNum];
  LGraph g;

  scanf("%d %d", &g->Nv, &g->Ne);
  for (int i=0; i<g->Ne; i++){
    scanf("%d %d", &ptrToAdjVNode[i]->AdjV, &ptrToAdjVNode[i]->Next);
  }
  return g;
}

bool TopSort( LGraph Graph, Vertex TopOrder[] )
{
  return true;
}
