### 1.mysql的索引的设计,索引和数据在mysql中是怎样存储的,mysql中有那些锁,各自可能会有哪些的场景
	1.首先是创建索引,考虑以下几个因素:1.覆盖索引,覆盖索引会减少mysql回表的次数,mysql5.6之后对覆盖索引进行了进一步的优化,支持索引下推(比如(name, age)),会先找出name对应的数据,然后在对age进行筛选然后回表,而不是查找到name直接回表.可以看explain(using index condition) 为了减少机械硬盘寻址的浪费,打开MRR(multi range read),可以在回表之前,把id读到buffer里面进行一个排序,把原来的随机操作变成一个顺序操作,这是覆盖索引可以做的一些优化.利用最左原则和覆盖索引配合,减少索引的维护.
	2. 普通索引,可以用到change buffer,change buffer将一些写操作缓存下来,在读到的时候进行merge的操作,提高写入的速度和内存的命中率.
	如果索引走不上,考虑哪些方面:
        1. sql问题,是否对索引字段进行了一些函数的操作
        2. 索引统计信息有问题,analyze table重新统计所有信息
        3. 可能业务表太多,内存的空洞比较多,都有可能造成内存的选择的问题.
        4. explain选出的索引不一定是最优的.

### 2.表的隔离级别
                                    脏读      不可重复读      幻读
    1.读未提交(read uncommitted)     允许         允许        允许
    2.读提交(read committed)         禁止         允许        允许
    3.可重复读(repeatable read)      禁止         禁止        允许
    4.串行化(serializable)           禁止         禁止        禁止
              假设有客户端A和客户端B同时开启事务
    1. 脏读(): 客户端B读取到了客户端A事务未提交的数据,客户端A回滚,造成脏读
    2. 不可重复读(同一条记录的内容被修改了,重点在于update或delete): 客户端B一条数据,此时客户端A修改该数据,客户端B再次读取读到的是客户端A修改之后的数据,此时就出现了"不可重复读"
    3. 幻读(查询某一范围的数据行变多了或者少了,终点站在于insert):客户端A查询表S中的所有数据,此时客户端B插入了一条新的数据,客户端A再次查询S表中的所有数据,发现多了一条,此时就出现了幻读

### 3.主从复制
主要涉及三个线程：binlog 线程、I/O 线程和 SQL 线程。

- binlog 线程: 负责将主服务器上的数据更改写入二进制日志(Binary log)中.
- I/O 线程: 负责从主服务器上读取二进制日志，并写入从服务器的中继日志(Relay log).
- SQL 线程: 负责读取中继日志，解析出主服务器已经执行的数据更改并在从服务器中重放(Replay).

### 4.读写分离
主服务器处理写操作以及实时性要求比较高的读操作，而从服务器处理读操作。

读写分离能提高性能的原因在于:

- 主从服务器负责各自的读和写，极大程度缓解了锁的争用.
- 从服务器可以使用 MyISAM，提升查询性能以及节约系统开销.
- 增加冗余，提高可用性.

读写分离常用代理方式来实现，代理服务器接收应用层传来的读写请求，然后决定转发到哪个服务器.

### 5.水平切分
水平切分又称为 Sharding，它是将同一个表中的记录拆分到多个结构相同的表中。

当一个表的数据不断增多时，Sharding 是必然的选择，它可以将数据分布到集群的不同节点上，从而缓存单个数据库的压力。



### 6.垂直切分
垂直切分是将一张表按列切分成多个表，通常是按照列的关系密集程度进行切分，也可以利用垂直切分将经常被使用的列和不经常被使用的列切分到不同的表中。

在数据库的层面使用垂直切分将按数据库中表的密集程度部署到不同的库中，例如将原来的电商数据库垂直切分成商品数据库、用户数据库等。