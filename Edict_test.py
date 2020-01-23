from Edict import Edict
a=Edict(xx=67,cn=81,a=5,kb=6,zc=8,d=9,e=30)
print("dict=",a)
a['kb']=23
print("setitem a['kb']=value")
print("valore cambiato",a)
print("getitem a['a']",a['a'])
print("\n slice esempi")
print("un solo valore a[:1] solo indice 0",a[:1])
print("indici tra due estremi a[1:5]=",a[1:5])
print("da 3 in poi a[3:]",a[3:])
a[:1]=10,# la virgola è necessaria  in quanto si tratta di tuple 
print('\nsetitem con slide a[:1]=10, oppure a[:1]=(10,) una sola voce la prima \n',a)
a[2:6]=(20,30,40,50) # se si toglie la virgola finale esclude lìultimo valore 50
print('\n a[2:]=20,30,40,50, oppure a[2:]=(20,30,40,50) \n',a)
print("\n List metodi in Edict")
print("\n ordine attuale delle chiavi\n",a)

a.reverse()
print("\n applico il metodo reverse\n",a,"\n")
a.sort()
print("\n applico il metodo sort\n",a,"\n")
a.sort(reverse=True)
print("\n applico il metodo sort sulla con  opzione reverse=True\n",a,"\n")
a.reorder()
print("\n applico il metodo reorder ritorna all'ordine orginale delle chiavi\n",a,"\n")
print("index posizione fisica di una chiave a.index('kb') da ",a.index('kb'))
print("\n metodo swap scambia le chiavi con i valori\n",a)
a.swap()
print("a.swap()\n",a)
a.swap()
print("di nuovo a.swap() ripristina il tutto\n",a)
print('\n Operazioni Set sulle chiavi')
b=Edict(xx=67,cnx=80,ab=5,kb=6,zc=8,cd=9,e=30)
print('\nmetodo union crea un nuovo dizionario con le chiavi di entrambi\
 in caso di collisione considera le chiavi del primo dizionario\n a.union(b)\n')
c=a.union(b)
print("a=",a,"\nb=",b,"\na.union(b)=",c)
print('\nmetodo intersection crea un nuovo dizionario con le chiavi comuni\n a.intersection(b)\n')
c=a.intersection(b)
print("a=",a,"\nb=",b,"\na.intersection(b)=",c)

print('\nmetodo difference crea un nuovo dizionario con le chiavi differenti presenti in a ma non in b\n a.difference(b)\n')
c=a.difference(b)
print("a=",a,"\nb=",b,"\na.difference(b)=",c)
     
print('\nmetodo symmetric_difference crea un nuovo dizionario con le chiavi di entrambi escluse le chiavi comuni a.(b)\nc=a.symmetric_difference(b)')
c=a.symmetric_difference(b)
print("a=",a,"\nb=",b,"\na.symmetric_difference(b)=",c)
c=Edict({'xx': 10, 'cn': 81, 'a': 20})
print("\nnuovo dizionario c=",c)
print("\n issuperset  ritorna True se il set contiene l'altro a.issuperset(c)=",a.issuperset(c))
      
print("\n issubset  ritorna True se un altro set è contenuto questo c.issubset(a)=",c.issubset(a))
      
print("\n isdisjoint ritorna True se i due set hanno intesezione nulla a.isdisjoint(c)=",a.isdisjoint(b))

      


      
