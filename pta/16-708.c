#include <stdio.h>
#include <stdlib.h>

typedef enum {false, true} bool;
#define MaxVertexNum 10  /* maximum number of vertices */
typedef int Vertex;      /* vertices are numbered from 0 to MaxVertexNum-1 */

typedef struct AdjVNode *PtrToAdjVNode;
struct AdjVNode{
    Vertex AdjV;
    PtrToAdjVNode Next;
};

typedef struct Vnode{
    PtrToAdjVNode FirstEdge;
} AdjList[MaxVertexNum];

typedef struct GNode *PtrToGNode;
struct GNode{
    int Nv;
    int Ne;
    AdjList G;
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
  int vertexNum, edgeNum;
  AdjList adjList;
  PtrToAdjVNode ptrToAdjVNode[MaxVertexNum];
  scanf("%d %d", &vertexNum, &edgeNum);
  for (int i=0; i<edgeNum; i++){
    scanf("%d %d", &ptrToAdjVNode[i]->AdjV, &ptrToAdjVNode[i]->Next);
    if (i==0){
      adjList.FirstEdge = ptrToAdjVNode[i];
    }
  }
  return adjList;
}

bool TopSort( LGraph Graph, Vertex TopOrder[] )
{
  return true;
}
