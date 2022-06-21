import tensorflow as tf

#TENSORES CONSTANTES (ESCALARES)
const_a = tf.constant(5) #const_a recebe o valor 5
const_b = tf.constant(9, dtype=tf.int32) #const_b recebe o valor 9 e é do tipo int32

#TENSORES RANDÔMICOS (ESCALARES)
rand_a = tf.random_normal([3], 2.0)
rand_b = tf.random_uniform([3], 1.0, 4.0)

#TENSORES CONSTANTES (MATRIZES)
mat_a = tf.constant([[2, 3], [9, 2], [4, 5]])
mat_b = tf.constant([[6, 4, 5], [3, 7, 2]])

#TENSORES VARIAVEIS
var = tf.Variable(tf.zeros([2,2])) #cria uma variavel
sess.run(tf.global_variables_initializer()) #inicializa ela como variavel

#CRIANDO PLACEHOLDER
a = tf.placeholder(tf.int32, shape=(3,1)) #diz p/ a máq.: reserva uma espaço da memória do tipo int32 c/ shape de (3,1)(o shape é opcional)
b = tf.placeholder(tf.float, shape=(1,3))
feed_dict={a:[[3],[2],[1]], b:[[1,2,3]]} #alimenta meus placeholder

#PREENCHIMENTO AUTOMATICO
tf.zeros([2,2]) #inicializa td com 0
tf.ones([2,2]) #inicializa td com 1

#ADIÇÃO
total = const_a + const_b
total = tf.add(const_a, const_b)

#SUBTRAÇÃO
diff = tf.subtract(rand_a, rand_b)

#DIVISÃO
div = tf.div(const_a, const_b)

#MULTIPLICAÇÃO
prod = tf.multiply(mat_a, mat_b)
prod = tf.matmul(mat_a, mat_b) #possui mais funcionalidades q a anterior

#SESSÃO (smp necessaria para executar um tensor; ha duas maneiras)
with tf.Session() as sess: #cria a sessão e ao terminar ja fecha
    print('\nA soma do node1 com o node2 é: %f' % sess.run(total))#executa o grafo

sess = tf.Session() #cria a sessão TF 
print("\nA soma do node1 com o node2 é:", sess.run(total)) #executa o grafo
sess.close() #fecha a sessão