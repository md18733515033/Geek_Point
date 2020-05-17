### 1. []的使用:
    Shell 里面的中括号（包括单中括号与双中括号）可用于一些条件的测试
    算术比较, 比如一个变量是否为0, [ $var -eq 0 ]
    文件属性测试，比如一个文件是否存在，[ -e $var ], 是否是目录，[ -d $var ]
    字符串比较, 比如两个字符串是否相同， [[ $var1 = $var2 ]]
    -gt	大于
    -lt	小于
    -ge	大于或等于
    -le	小于或等于
    [ -f $file_var ]	    变量 $file_var 是一个正常的文件路径或文件名 (file)，则返回真
    [ -x $var ]	            变量 $var 包含的文件可执行 (execute)，则返回真
    [ -d $var ]	            变量 $var 包含的文件是目录 (directory)，则返回真
    [ -e $var ]	            变量 $var 包含的文件存在 (exist)，则返回真
    [ -c $var ]	            变量 $var 包含的文件是一个字符设备文件的路径 (character)，则返回真
    [ -b $var ]	            变量 $var 包含的文件是一个块设备文件的路径 (block)，则返回真
    [ -w $var ]	            变量 $var 包含的文件可写(write)，则返回真
    [ -r $var ]	            变量 $var 包含的文件可读 (read)，则返回真
    [ -L $var ]	            变量 $var 包含是一个符号链接 (link)，则返回真
    [[ $str1 != $str2 ]]    如果 str1 与 str2 不相同，则返回真
    [[ -z $str1 ]]          如果 str1 是空字符串，则返回真
    [[ -n $str1 ]]	        如果 str1 是非空字符串，则返回真
    -b file	检测文件是否是块设备文件，如果是，则返回 true。	[ -b $file ] 返回 false。
    -c file	检测文件是否是字符设备文件，如果是，则返回 true。	[ -c $file ] 返回 false。
    -d file	检测文件是否是目录，如果是，则返回 true.         [ -d $file ] 返回 false。
    -f file	检测文件是否是普通文件（既不是目录，也不是设备文件），如果是，则返回 true。	[ -f $file ] 返回 true。
    -g file	检测文件是否设置了 SGID 位，如果是，则返回 true。	[ -g $file ] 返回 false。
    -k file	检测文件是否设置了粘着位(Sticky Bit)，如果是，则返回 true。	[ -k $file ] 返回 false。
    -p file	检测文件是否是有名管道，如果是，则返回 true。	                [ -p $file ] 返回 false。
    -u file	检测文件是否设置了 SUID 位，如果是，则返回 true。	        [ -u $file ] 返回 false。
    -r file	检测文件是否可读,如果是,则返回 true.	                    [ -r $file ] 返回 true。
    -w file	检测文件是否可写,如果是,则返回 true.	                    [ -w $file ] 返回 true。
    -x file	检测文件是否可执行，如果是，则返回 true。	                [ -x $file ] 返回 true。
    -s file	检测文件是否为空（文件大小是否大于0）,不为空返回 true.     	[ -s $file ] 返回 true。
    -e file	检测文件（包括目录）是否存在，如果是，则返回 true。	        [ -e $file ] 返回 true。
    -nt 判断file1是否比file2新  [ "/data/file1" -nt "/data/file2" ]
    -ot 判断file1是否比file2旧  [ "/data/file1" -ot "/data/file2" ]

### 2.重定向
    > 重定向输出到某个位置，替换原有文件的所有内容。
    
    >> 重定向追加到某个位置，在原有文件的末尾添加内容。
    
    < 重定向输入某个位置文件。
    
    2> 重定向错误输出。
    
    2>> 重定向错误追加输出到文件末尾。
    
    &> 混合输出错误的和正确的都输出。
    
### 3.let命令
let 命令是 BASH 中用于计算的工具，用于执行一个或多个表达式，变量计算中不需要加上 $ 来表示变量。如果表达式中包含了空格或其他特殊字符，则必须引起来。
    
    a=5
    let a++

### 4.函数中$符的使用
    $#	传递到脚本或函数的参数个数
    $*	以一个单字符串显示所有向脚本传递的参数
    $$	脚本运行的当前进程ID号
    $!	后台运行的最后一个进程的ID号
    $@	与$*相同，但是使用时加引号，并在引号中返回每个参数。
    $-	显示Shell使用的当前选项，与set命令功能相同。
    $?	显示最后命令的退出状态。0表示没有错误，其他任何值表明有错误。