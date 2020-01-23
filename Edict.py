##########################################################
# Classe    : Edict                                      #
# Scopo     : estende un dizionario standart             #
# Autore    : Marco Salvati                              #
# Email     : salvatimarco61@gmail.com                   #
# Licenza   : GPL 3                                      #
# Data      : 2019-11-04                                 #
########################################################## 
class Edict(dict):
    def __init__(self,cnf={},**kargs):
        """
        Classe    : Edict
        Scopo     : estende un dizionario standart, ricorda l'ordine di inserimento
                    delle chiavi, implementa metodi delle liste e metodi set
        Autore    : Marco Salvati
        Email     : salvatimarco61@gmail.com
        Licenza   : GPL 3
        Data      : 2019-11-04
        """
        self.klist=[]
        self.order=[]
        self.__dict={}
        
        if len(kargs):
            for k,v in kargs.items():
                self.klist.append(k)
                self.order.append(k)
                self.__dict[k]=v
                
        elif cnf!={}:
            self.__dict=cnf
            self.klist=[x for x in self.__dict.keys()]
            self.order=[x for x in self.__dict.keys()]
    
    def __getitem__(self,key_item):
         """ Oltre al classico metodo dei dizionari implementa lo slice delle liste
             es: d[1:6] ritorna un dizionario con le chiavi da 1 a 5 rispetto l'ordine
             di inserimento """
         if isinstance(key_item,slice):
             d={}
             l=self.klist[key_item]
             for k in l:
                 d[k]=self.__dict[k]
             return Edict(d)    
         else:
             return self.__dict[key_item]
    def __setitem__(self, key_item, *value):
        """ Oltre al classico metodo dei dizionari implementa lo slice delle liste
             es: d[1:4]="Cane","Gatto","Pulce" inserisce i valori nelle chiavi da 1 a 3 rispetto l'ordine
             di inserimento """
        if isinstance(key_item,slice):
            d,i,v={},0,list(*value)
            l=self.klist[key_item]
            for k in l:
                self.__dict[k]=v[i]
                i+=1     
        else:
            if key_item not in self.klist:
                self.klist.append(key_item)
                self.order.append(key_item)
            self.__dict[key_item]=value[0]
    def __delitem__(self, key_item):
        """ Oltre al classico metodo dei dizionari implementa lo slice delle liste
             es: del(d[1:4]) elimina le chiavi da 1 a 3 rispetto l'ordine
             di inserimento """
        if isinstance(key_item, slice):
            l=self.klist[key_item] # prendi le chiavi interessate
            for i in l: # cancella le chiavi dal dizionario
                del self.__dict[i]
            del self.keylist[key_item] # cancella le chiavi dalla lista
        else: # cancella la chiave del dizionario
            del(self.__dict[key_item])
    def keys(self):
        """ritorna le chiavi del dizionario"""
        return iter(self.klist)
    def values(self):
        """ritorna i valori del dizionario"""
        return iter([self.__dict[x] for x in self.klist])
    def items(self):
        """ritorna le chiavi e valori del dizionario"""
        return iter([(x,self.__dict[x]) for x in self.klist])
    # operazioni tipo lista
    def reorder(self):
        """riordina le chiavi del dizionario nell'ordine in cui sono state inserite"""
        self.klist=self.order.copy()
        t=dict()
        for i in self.order:
            t[i]=self.__dict[i]
        self.__dict=t.copy()
    def reverse(self):
        """Invertisce l'ordine delle chiavi"""
        self.klist.reverse()
        t=dict()
        for i in self.klist:
            t[i]=self.__dict[i]
        self.__dict=t.copy() 
    def sort(self,reverse=False):
        """sort delle chiavi"""
        t=dict()
        self.klist.sort(reverse=reverse)
        for i in self.klist:
            t[i]=self.__dict[i]
        self.__dict=t.copy()
    def index(self,key):
        """ritorna la posizione della chiave"""
        return self.klist.index(key) 
    def __len__ (self):
        """ritorna il numero delle chiavi"""
        return len(self.__dict)
    def __contains__(self, key):
        """operatore in """
        return key in self.klist
    # operatori di confronto
    def  __eq__(self, value):
        """op. uquale"""
        return self.__dict==value.__dict
    def  __qe__(self, value):
        """op. maggiore e uquale"""
        return self.__dict>=value.__dict
    def  __qt__(self, value):
        """op. maggiore"""
        return self.__dict>value.__dict
    def  __le__(self, value):
        """op. minore e uquale"""
        return self.__dict<=value.__dict
    def  __lt__(self, value):
        """op. minore"""
        return self.__dict<value.__dict
    def  __ne__(self, value):
        """op. diverso"""
        return self.__dict!=value.__dict
    """ operazioni dict a str"""
    def __repr__(self):
        return repr(self.__dict)
    def __str__(self):
        return str(self.__dict)
    def __sizeof__(self):
        return seld.dict.__sizeof__()
    def clear(self):
        """metodo clear"""
        self.klist.clear()
        self.klist.order()
        self.__dict.clear()
    """ metodi dizionari"""    
    def copy(self):
        t=Edict()
        t.klist=self.klist.copy()
        t.dict=self.__dict.copy()
        return t
    def fromkeys(iterable, value=None):
        """"Ritorna un nuovo dict con chiavi da un iteratore e valori uguali a value."""
        self.klist=[x for x in iterable]
        self.__dict.fromkeys(iterable,value)
    def get(self, key, default=None):
        """ Ritorna il valore di una chiave se la chiave è nel dizionario, altrimenti ritorna default."""
        return self.__dict.get(key,default)
    def pop(self, k ,d=None):
        """ Se la chiave non è presente, ritorna d se presente, altrimenti avviene un KeyError"""
        if k in self.klist:
            ind=self.klist.index(k)
            self.klist=self.klist[:ind]+self.klist[ind+1:]
            self.order=self.order[:ind]+self.order[ind+1:] 
            return self.__dict.pop(k,d)
    def popitem(self):
        """ D.popitem() -> (k, v), rimuove e ritorna una coppia chiave valore"""
        """ 2-tuple; ma esegue un KeyError se D è vuoto."""
        self.klist=self.klist[:-1]
        self.order=self.order[:-1]
        return self.__dict.popitem()
        
    def setdefault(self, key, default=None):
        """Inserisce una chiave con un valore di default se la chiave non è nel dizionario."""
        #Return the value for key if key is in the dictionary, else default.
        self.__dict.setdefault(key, default)
        if key not in self.klist:
            self.klist.append(key)
            self.order.append(key)
            
    def update(self,E=None,**F):
        "effettua l' update delle chiavi del dizionario"
        self.__dict.update(E,**F)
        self.klist=[x for x in self.__dict.keys()]
        self.klist=[x for x in self.__dict.keys()]
    def swap(self):
        """invertisce le chiavi con i suoi valori"""
        k=[x for x in self.__dict.values()]
        kv=[x for x in self.__dict.items()]
        self.klist=[x for x in k]
        self.order=[x for x in k]
        self.__dict={v:k for k,v in kv}
    # set operazioni sulle chiavi ##############
    def union(self,other):
        """ ritorna un nuovo dizionario dall'operazione di union sulle chiavi con un altro"""
        s1,s2,d=set(self.klist),set(other.klist),dict()
        s=s1.union(s2)
        for i in s:
            if i in self.klist:
                d[i]=self.__dict[i]
            else:
                d[i]=other.__dict[i]
        return Edict(d)
    def intersection(self,other):
        """ ritorna un nuovo dizionario dall'operazione di intersection sulle chiavi con un altro"""
        s1,s2,d=set(self.klist),set(other.klist),dict()
        s=s1.intersection(s2)
        for i in s:
            if i in self.klist:
                d[i]=self.__dict[i]
            else:
                d[i]=other.dict[i]
        return Edict(d)
    def difference(self,other):
        """ ritorna un nuovo dizionario dall'operazione di difference sulle chiavi con un altro"""
        s1,s2,d=set(self.klist),set(other.klist),dict()
        s=s1.difference(s2)
        for i in s:
            if i in self.klist:
                d[i]=self.__dict[i]
            else:
                d[i]=other.dict[i]
        return Edict(d)
    def symmetric_difference(self,other):
        """ ritorna un nuovo dizionario dall'operazione di symmetric_difference sulle chiavi con un altro"""
        s1,s2,d=set(self.klist),set(other.klist),dict()
        s=s1.symmetric_difference(s2)
        for i in s:
            if i in self.klist:
                d[i]=self.__dict[i]
            else:
                d[i]=other.__dict[i]
        return Edict(d)
    def issuperset(self,other):
        """ritorna True se le chiavi di un dizionario sono un superset di un altro"""
        s1,s2,d=set(self.klist),set(other.klist),dict()
        return s1.issuperset(s2)        
    def issubset(self,other):
        """ritorna True se le chiavi di un dizionario sono un subset di un altro"""
        s1,s2,d=set(self.klist),set(other.klist),dict()
        return s1.issubset(s2)        
    def isdisjoint(self,other):
        """ritorna True se le chiavi di un dizionario sono diverse da un altro"""
        s1,s2,d=set(self.klist),set(other.klist),dict()
        return s1.isdisjoint(s2)        
   
