import matplotlib.pyplot as plt
from random import *
from math import *

##Classes utilisees

class Point(object):
    def __init__(self,abs,ord):
        self.x = abs
        self.y = ord
        self.cutEdge ='not yet computed'

    def __repr__(self):
        """surcharge du repr() """
        return "Point: abscisse:{}, ordonné:{}".format(self.x, self.y)

    def __str__(self):
        """surcharge du print() """
        return "({},{})".format(self.x, self.y)

    def affichePoint(self,type='bo'):
        plt.plot(self.x,self.y, type)

    def dist(self,other):
        return sqrt((self.x-other.x)**2+(self.y-other.y)**2)

class Edge():
    def __init__(self,endp1,endp2):
        self.endp1 = endp1
        self.endp2 = endp2

    def afficheEdge(self,param='b'):
        plt.plot([self.endp1.x,self.endp2.x],[self.endp1.y,self.endp2.y],param)

class ChEdge(Edge):
    #Cree une srtucture de liste chainee sur l'enveloppe convexe
    def __init__(self,endp1,endp2,next=None,prev=None):
        Edge.__init__(self, endp1,endp2)
        self.next=next
        self.prev=prev

    def addAfter(self,other):
        #ajoute self apres other
        self.prev=other
        self.next=other.next
        other.next.prev=self
        other.next=self

    def suppressEdge(self):
        self.next.prev=self.prev
        self.prev.next=self.next


##Fonctions annexes

def updateCutEdge(point,wE,center):
    # Met a jour posH (image de point par la fonction T)
    # pour un convexe contenant l arete wE
    #renvoie 'inside' ou l'arete coupee
    cutEdge=None
    edge=wE
    while "Tant que l on ne retombe pas sur wE ou que l on n a pas trouve l arete coupee":
        p=interLine(edge,Edge(point,center))
        if p.x<max(center.x,point.x) and p.x>min(center.x,point.x):
            cutEdge=edge
            break
        edge=edge.next
        if edge==wE:
            break
    point.cutEdge=cutEdge

def interLine(edge1, edge2):
    # Point d'intersection des droite AB et CD
    (x_a, y_a) = (edge1.endp1.x, edge1.endp1.y)
    (x_b, y_b) = (edge1.endp2.x, edge1.endp2.y)
    (x_c, y_c) = (edge2.endp1.x, edge2.endp1.y)
    (x_d, y_d) = (edge2.endp2.x, edge2.endp2.y)
    a1 = (y_a - y_b) / (x_b - x_a)
    c1 = y_a + a1 * x_a
    a2 = (y_c - y_d) / (x_d - x_c)
    c2 = y_c + a2 * x_c
    y = (c2 * a1 - c1 * a2) / (a1 - a2)
    x = (c1 - y) / a1
    return Point(x, y)

def dotProd(c,p1,p2):
    #renvoie le produit determinant(orientation) des vecteurs cp1 et cp2
    return (p1.x-c.x)*(p2.y-c.y)-(p1.y-c.y)*(p2.x-c.x)

# plot en mode iteratif
plt.ion()

## Calcul de l enveloppe convexe
def convexHull(liPT):
    #Entrée: liste de points
    #Sortie: Une arete chainee de l'enveloppe convexe

    #Initialisation (premier Triangle)
    P=liPT[0:3]
    for p in P: liPT.remove(p)
    T=[ChEdge(P[i-1],P[i]) for i in range(3)]
    for i in range(3): # init de la liste chainee
        T[i-1].next=T[i]
        T[i].prev=T[i-1]
    wEdge=T[0] # wEdge pour arete temoin (witness edge)
    c=Point(sum([i.x for i in P])/3,sum([i.y for i in P])/3) #bary du triangle initial
    for p in liPT: updateCutEdge(p,wEdge,c) # Update initiale

    # On boucle tant qu il reste de sommets non visites
    while liPT!=[]:
        i=randint(0,len(liPT)-1)
        p=liPT.pop(i) #nouveau sommet visite A randomiser
        P+=[p]
        if p.cutEdge==None: continue # si on a choisit un point interieur, on passe a un autre

        #Affichage graphique des point (bleu=visites, vert=centre, jaune=nouveau, rouge= non visite)
        # Et des arete de Convexe Hull
        c.affichePoint('go')
        for pt in liPT: pt.affichePoint('ro')
        for pt in P: pt.affichePoint()
        p.affichePoint('yo')
        edge=wEdge
        while "Tant que l on ne retombe pas sur wEdge":
            edge.afficheEdge()
            edge=edge.next
            if edge==wEdge: break

        # Calcul des aretes a retirer(visibilite V de p (rouge et jaunes))
        e_0=p.cutEdge #arete coupee par p
        e_0.afficheEdge('r')
        V=[e_0]# On construit V
        e_right = e_0.next
        e_left = e_0.prev
        dotP = dotProd(p, e_0.endp1, e_0.endp2)
        dotP1 = dotProd(p, e_right.endp1, e_right.endp2)
        while dotP1*dotP > 0:
            V += [e_right]
            e_right.afficheEdge('y')
            e_right = e_right.next
            dotP1 = dotProd(p, e_right.endp1, e_right.endp2)
        dotP2 = dotProd(p, e_left.endp1, e_left.endp2)
        while dotP2*dotP > 0:
            V += [e_left]
            e_left.afficheEdge('y')
            e_left = e_left.prev
            dotP2 = dotProd(p, e_left.endp1, e_left.endp2)
        wEdge=ChEdge(p,e_right.endp1)
        wEdge.addAfter(e_right.prev)
        ChEdge(e_left.endp2,p).addAfter(e_left)
        for e in V:
            e.suppressEdge()

        plt.pause(1)
        plt.clf()
        #Mise a jour
        for p in liPT: updateCutEdge(p,wEdge,c)

    #Sortie de boucle, affichage final
    edge=wEdge
    while "Tant que l on ne retombe pas sur wEdge":
        edge.afficheEdge()
        edge=edge.next
        if edge==wEdge: break
    for pt in P: pt.affichePoint()
    input('Press a enter to quit')
    #plt.show()
    return wEdge

if __name__=="__main__":
    n=int(input('Nombre de points: '))
    liP=[Point(random(),random()) for i in range(n)]
    conveXH= convexHull(liP)

