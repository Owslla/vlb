Intro
=====

> Other way to explain *Practical-Vim-Edit-Text-at-the-Speed-of-Thought.pdf*

>学习之前你必需知道什么是VIM,和常见的模式.


> 按键约定 

||表示|| 意思||
||X|| Press X once||
||dw||In sequence, press d , then w||
||dap||In sequence, press d , a , then p||
||< C-n>|| Press < Ctrl> and n at the same time||
|| g< C-]>|| Press g , followed by < Ctrl> and ] at the same time||
||< C-r>0|| Press < Ctrl> and r at the same time, then 0||
||< C-w>< C-=>|| Press < Ctrl> and w at the same time, then < Ctrl> and = at the same time||
||f{char}|| Press f , followed by any other character||
||`{a-z}|| Press ` , followed by any lowercase letter||
||m{a-zA-Z}|| Press m , followed by any lowercase or uppercase letter||
||d{motion}|| Press d , followed by any motion command||
||< C-r>{register}|| Press < Ctrl> and r at the same time, followed by the address of a register||
||< Esc>|| Press the Escape key||
||< CR>|| Press the carriage return key (also known as <Enter> )||
||< Ctrl>|| Press the Control key||
||< Tab>|| Press the Tab key||
||< Shift>|| Press the Shift key||
||< S-Tab>|| Press the <Shift> and <Tab> keys at the same time||
||< Up>|| Press the up arrow key||
||< Down>|| Press the down arrow key||
||␣|| Press the space bar||
>提示如果你在表格最后一行看到方框说明你的编辑器不支持UTF16

<p>




> VI 家族

>假如你和我一样对一个开源的事物非常感兴趣那么我们一起来分享一下,VI的大家族  
>成员吧, *ex*是原始的unix 编辑器那时候还不兴盛显示器,几乎是和电报机的输入是  
>是一个年代,后来才有了*ed*,有了可视化使编辑器后才有了*em**en*ex ,当有了visual   
>才真正的有了*vi*,*vim*就是improved.参见[wiki](http://en.wikipedia.org/wiki/Teleprinter)

> 获取帮助
在所有普通模式下(normal)输入:h sth


Content
----
>此部分讲述所有重要的Tips,以练习的方式,部分讲解不到位的可与[我](zzepaigh@gamil.com)交流,也可以参原文档  


**Tip1 使用. 命令(Meet the Dot Command)** 

> . 命令几乎可以是vim最常用的命令之一(除了< Esc>之外),作用是重复最后一次更改,  
> 类似于CAD中的空格键.  

---
    original
Line one  
Line two  
Line three  
Line four  

    keystrokes
`x...`


    result
<p>

    one  
    Line two  
    Line three  
    Line four  

> original:你可以用u来回退(undo)

---
    original
Line one  
Line two  
Line three  
Line four  

    keystrokes
`dd..`

    result
<p>

    Line three  
    Line four  

---
    original
Line one  
Line two  
Line three  
Line four  

    keystrokes
`j>Gj.j.`

    result
<p>

    Line one  
        Line two  
            Line three  
                Line four  

**Tip2 不要自己重复做(Don't Repeat Yourself)**

----
    original
var foo = 1  
var bar = 'a'  
var foobar = foo + bar  

    keystrokes
`A;< Esc>j.j.`

    result
<p>

    var foo = 1;  
    var bar = 'a';  
    var foobar = foo + bar;

> 提示:你可能得到结果是分号前有两个空格，那是因为markdown语法差异  
> 如果你自行构建原始文本的话，就能得到相同的结果  

*一代二* 功效表

||一个键||两个键||
||C||c$||
||s||cl||
||S||^C||
||I||^i||
||A||$a||
||o||A< CR>||
||O||ko||


**Tip3 做一次,然后重复(Take One Step Back, Then Three Forward)**

---
    original
var foo = "method("+argument1+","+argument2+")";

    keystrokes 
`f+s␣+␣< Esc>;.;.;.`

    result
<p>

    var foo = "method(" + argument1 + "," + argument2 + ")";

> Explain ;表示重演上一次搜索.

**Tip4 执行,重复,回退(Act, Repeat, Reverse)**
>写在前面的话,小写的u就是精髓表示undo.当然更多请看表。

*更改的执行，重复来回退* 对照表

||Intent || Act || Repeat || Reverse||
||Make a change || {edit} || .  || u||
||Scan line for next character || f{char} / t{char} || ; || ,||
||Scan line for previous character || F{char} / T{char} || ; || ,||
||Scan document for next match || /pattern <CR> || n || N||
||Scan document for previous match ?pattern<CR> || n || N||
||Perform substitution || :s/target/replacement || & || u||
||Execute a sequence of changes || qx{changes}q || @x || u||

**Tip5 手动查找替换 (Find and Replace by Hand)**

---

    original
...We're waiting for content before the site can go live...  
...If you are content with this, let's go ahead with it...  
...We'll launch as soon as we have the content...    

    keystrokes(注意以:开头是VIM的命令行模式)
`:182,185s/content/copy/g`

or

`:182.185s@content@copy@g`

    result
<p>

    ...We're waiting for copy before the site can go live...  
    ...If you are copy with this, let's go ahead with it...  
    ...We'll launch as soon as we have the copy...    

> 你可以要调整:182.185s 为original文本的的行号

---

    original
...We're waiting for content before the site can go live...  
...If you are content with this, let's go ahead with it...  
...We'll launch as soon as we have the content...    

    keystrokes
{start}光标在content的c字母上（本教程所以未指明{start}的都在original的最开头）
`*cwcopy< Esc>n.`

    result
<p>

    ...We're waiting for content before the site can go live...  
    ...If you are copy with this, let's go ahead with it...  
    ...We'll launch as soon as we have the copy...    

**Tip6 尽量使用.命令 (Meet the Dot Formula)**

---
reference Tip2

**Tip7**

---
reference原文档 

**Tip 打点你的回退(Chunk Your Undos)**
>这个很简单就是用u进行undo,这里主要讲什么会生成你的Undo列表,用的多自行发现吧  

---
但是这里有个非常重要的知识点，
> 当你在Insert mode里面用Up Down Left Right也会生成undo事件点。

**Tip9 提交可重复的更改(Compost Repeatab Changes)**

---
    original
The end is nigh

    keystrokes
光标{start}@The的T上面
`$dbx`

    result
<p>

    The end is 

---
    original
The end is  nigh

    keystrokes
光标{start}@The的T上面
`$bdw`

    result
<p>

    The end is 

---
    original
The end is  nigh

    keystrokes
光标{start}@The的T上面
`$daw`

    result
<p>

    The end is 


> 以上方法最后一个更妙，因为可以使用. repeat

**Tip10  简单计算(User Counts Do simple Arithmetic)**
> 使用< C-a>和< C-x> .

---

    original

.blog, .news { background-image: url(/sprite.png); }  
.blog { background-position: 0px 0px }

    keystrokes
`jyypcW.news< Esc>180< C-x>`

    result
<p>

    .blog, .news { background-image: url(/sprite.png); }
    .blog { background-position: 0px 0px }
    .news { background-position: -180px 0px }

> 关于数字格式化的趣事，*007* < c-a>后不是*008* 而是*010*

**Tip11 不要去计算除非你要重复操作(Don't Count If You Can Repeat)**

---

    original
I have a couple of questions.

    keystrokes
    鼠标{start}@a couple的a上面
`c3wsome more< Esc>`

    result
<p>

    I have some more questions.

---

    original
I have a couple of questions.

    keystrokes
    鼠标{start}@a couple的a上面
`daw..isomemore< Esc>`

    result
<p>

    I have some more questions.

>使用第二种的原因是可以不用计数，可以用u逐个回退

**Tip12 组合(Combine and Conquer)**

黄金法则
---
Operator + Motion =Action

*vim操作命令* 表

||按键||效果||
||c|| Change||
||d|| Delete||
||y|| Yank into register||
||g~|| Swap case||
||gu|| Make lowercase||
||gU|| Make uppercase||
||>|| Shift right||
||<|| Shift left||
||=|| Autoindent||
||!|| Filter {motion} lines through an external program||

**Tip13 Insert 模式下的迅速更正(Make Corrections Instantly from Insert Mode)**
> 正如标题所说的一样是在插入模式入的

> *按键表*


||< C-h>|| Delete back one character (backspace)||
||< C-w>|| Delete back one word||
||< C-u>|| Delete back to start of line||

**Tip14 返回常规模式(Get Back to Normal Mode)**
> 你懂的都很简单，看下表

||按键||效果||
||< Esc>|| Switch to Normal mode||
||< C-[>|| Switch to Normal mode||
||< C-o>|| Switch to Insert Normal mode||

> 为什么会有个Insert Normal  mode呢，请接着看

    当我们在编辑文本的时候经常会写写就到了编辑器的底部，在常规模式下可以使用
    zz，使编辑区在屏幕的中央,但不要鼠标，但是在插入模式下你用zz后肯定会输入
    zz这两个字符，为了实现需求我们不需要退到Normal mode-->zz-->再进入
    Insert mode.  而是可以进入一个过度mode叫做Insert Normal Mode,这样
    就能在INsert mode下使用 zz. 自行演示，不理解请google,或者沟通.

**Tip15从注册区中粘贴而不离开Insert Mode (Paste From a Register Without Leaving Insert mode)**

>(see :h i_CTRL-R ).  
>(see :h i_CTRL-R_CTRL-P ).

---

    original
Practical Vim, by Drew Neil  
Read Drew Neil's

    keystrokes
`yt,jA␣< C-r>0.< Esc>`

    result
<p>

    Practical Vim, by Drew Neil  
    Read Drew Neil's Practical Vim.

**Tip16 要自己看了，翻译不来(DoBack-of-the-EnvelopeCalculations in Place)**

---

    original
6 chairs, each costing $35, totals $

    keystrokes
`A< C-r>=6*35< CR>`
    
    result
<p>

    6 chairs, each costing $35, totals $210


**Tip17输入非常规字符(Insert Unusual Characters By Character Code)**

>你可以输入✓½这样的更多字符当然,当然要有字符集,看
 See: h i_CTRL-V_digit

*非常规输入* 表

||Keystrokes ||Effect||
||< C-v>{123} ||Insert character by decimal code||
||< C-v>u{1234} ||Insert character by hexadecimal code||
||< C-v>{nondigit} ||Insert nondigit literally||
||< C-k>{char1}{char2} ||Insert character represented by {char1}{char2} digraph||


**Tip18 通过二全字母插入非常规字符(Insert Unusual Characters by Digraph)**

Ĩ✓
> : h digraph-table 

**Tip19 在Replace Mode下替换存在的文本(Overwirte Existing Text with Replace Mode)**

---
 
    original
Typing in Insert mode extends the line. But in Replace mode  
the line length doesn't change.

    keystrokes
`f.R, b< Esc>`

    result
<p>

    Typing in Insert mode extends the line, but in Replace mode
    the line length doesn't change.

**Tip 20  Grok Visual Mode**

---
无

**Tip21 定义一个Visual区(Define a Visual Selection)**

*区域定义*表

||Command|| Effect||
||v|| Enable character-wise Visual mode||
||V|| Enable line-wise Visual mode||
||< C-v>|| Enable block-wise Visual mode||
||gv|| Reselect the last visual selection||

*visual 切换法*表

||< Esc> / ||Switchto Normal mode||
||< C-[> ||Switch to Normal mode (when used from character-, line- or||
||v / V / ||Switch to character-wise Visual mode||
||< C-v> ||Switch to line-wise Visual mode||
||v ||Switch to block-wise Visual mode||
||V ||Go to other end of highlighted text||
||< C-v> ||block-wise Visual mode, respectively)||
||o ||Go to other end of highlighted text||

---

    original
Select from here to here.

    keystrokes
    鼠标{start}@第二个here的第一个h上.
`vbboe`

    result
<p>

    Select from here to here.
    ____________xxxxxxxxxxxx.

>注:以上x表示选中，__表示未选中.

**Tip 22 重复行选择命令(Repeat Line-Wise Visual Commands)**

---

    original
def fib(n):
    a, b = 0, 1
    while a < n:
print a,
a, b = b, a+b
fib(42)

    keystrokes
    鼠标{start}@第一个print的p上
`Vj>.`

    result

<p>

    def fib(n):
        a, b = 0, 1
        while a < n:
            print a,
            a, b = b, a+b
    fib(42)


> 如果你得到的缩进不对,请设置 :set shiftwidth=4 softtabstop=4 expandtab
> 不清楚请自行google或者找我



**Tip23尽可能得使用Visual命令(Prefer Operators to Visual Commands where Possible)**

---
    
    original

    <a href="#">one</a>  
    <a href="#">two</a>   
    <a href="#">three</a>  

    keystrokes
`vitUj.j.`

    result

    <a href="#">ONE</a>  
    <a href="#">TWO</a>   
    <a href="#">THRee</a>  

---

    original

    <a href="#">one</a>  
    <a href="#">two</a>   
    <a href="#">three</a>  

    keystrokes
`gUitj.j.`

    result
<p>

    <a href="#">ONE</a>  
    <a href="#">TWO</a>   
    <a href="#">THREE</a>  


**Tip24 使用Visual-Block快速表格化(Edit Tabular Data with Visual-Block MOde)**

---

    original

Chapter                 Page  
Normal mode             15   
Insert mode             31  
Visual mode             44  

    keystrokes
    鼠标{start}@Chapter和Page之间
`< C-v>3jx...gvr|yypVr-`

    result
<p>

    Chapter         |  Page  
    -------------------------
    Normal mode     |  15   
    Insert mode     |  31  
    Visual mode     |  44  

**Tip 25改变字段内的文本(Change Columns of Text)**

---

    original

li.one      a{ background-image: url('/images/sprite.png'); }   
li.two      a{ background-image: url('/images/sprite.png'); }   
li.three    a{ background-image: url('/images/sprite.png'); }   

    keystrokes
鼠标{start}@第一行/image的i字母上
` < C-v>jjeccomponents< Esc>`

    result
<p>

li.one      a{ background-image: url('/components/sprite.png'); }   
li.two      a{ background-image: url('/components/sprite.png'); }   
li.three    a{ background-image: url('/components/sprite.png'); }   
 
**Tip26 追加在最后(Append After a Ragged Visual Block)**
>正好前面.命令的例子

---

    original
var foo = 1  
var bar = 'a'  
var foobar = foo + bar  

    keystrokes
    鼠标{start}@第一行的1数字上
`< C-v>jj$A;`

    result
<p>

    var foo = 1  ;
    var bar = 'a'  ;
    var foobar = foo + bar  ;

**趣味历史**

    In the beginning, there was ed. ed begat ex, and
    ex begat vi, and vi begat Vim.
        ➤ The Old Testament of Unix

**Tip27初见Vim的命令行(Meet Vim's Command Line)**

||Command|| Effect||
||:[range]delete [x] ||Delete specified lines [into register x]||
||:[range]yank [x] ||Yank specified lines [into register x]||
||:[line]put [x] ||Put the text from register x after the specified line||
||:[range]copy {address} ||Copy the specified lines to below the line specified by {address}||
||:[range]move {address} ||Move the specified lines to below the line specified by {address}||

||:[range]join ||Join the specified lines || 
||:[range]normal {commands} ||Execute Normal mode {commands} on each specified line||
||:[range]substitute/{pattern}/{string}/[flags] ||Replace occurrences of {pattern} with {string} on each specified line||
||:[range]global/{pattern}/[cmd] ||Execute the Ex command [cmd] on all specified lines where the {pattern} matches||

**Tip28 执行一条命令多行生效(Execute a Command on One or More Consecutive Lines)** 

---
    original 
    Line1 <!DOCTYPE html>
        2 <html>
        3   <head><title>Practical Vim</title></head>
        4   <body><h1>Practical Vim</h1></body>
        5 </html>
<p>

    keystrokes 1
`:1`  

`:print`

    commandline result 1
<p>

        Line1 <!DOCTYPE html>
<p>
    keystrokes 2 

`:663`  
`:p`

    commandline result 2
        5 </html>

<p>
    keystrokes 3

`:661p`

    commandline result 3
        3   <head><title>Practical Vim</title></head>

<p>
    keystrokes 4

`:661,663p`

    commandline result 4
        3   <head><title>Practical Vim</title></head>
        4   <body><h1>Practical Vim</h1></body>
        5 </html>


> 注:本章节中有 $ 和 % 之类的定位符，因为内嵌教程,不能演示请自行单独文本操作

---
    original
    
    <!DOCTYPE html>
    <html>
        <head><title>Practical Vim</title></head>
        <body><h1>Practical Vim</h1></body>
    </html>
<p>

    keystrokes
    行虚拟块选中原始文档中的第二到最后一行
`:'<,'>p`

    commandline result
    
    <html> 
       <head><title>Practical Vim</title></head>
       <body><h1>Practical Vim</h1></body>
    </html>


---
    original
    
    <!DOCTYPE html>
    <html>
        <head><title>Practical Vim</title></head>
        <body><h1>Practical Vim</h1></body>
    </html>
<p>

    keystrokes
`:/<html>/,/<\/html>/p`

    commandline result
    
    <html> 
       <head><title>Practical Vim</title></head>
       <body><h1>Practical Vim</h1></body>
    </html>


---
    original
    
    <!DOCTYPE html>
    <html>
        <head><title>Practical Vim</title></head>
        <body><h1>Practical Vim</h1></body>
    </html>
<p>

    keystrokes

` :/<html>/+1,/<\/html>/-1p `

    commandline result 

        <head><title>Practical Vim</title></head>
        <body><h1>Practical Vim</h1></body>

**Tip29 使用':t'and ':m'命令重复或者移动和(DuplicateorMoveLinesUsing‘:t’and ‘:m’Commands
)**

> 重复类似于复制但不是copy而是duplicater

---
    original

    Line 1 Shopping list
         2     Hardware Store
         3         Buy new hammer
         4 Beauty Parlor
         5      Buy nail polish remover
         6      Buy nails
    

<p>

    keystrokes
    鼠标{start}@Hardware的H上
`:6copy.`

    result

    Line 1 Shopping list
         2     Hardware Store
         6         Buy nails
         3         Buy new hammer
         4 Beauty Parlor
         5      Buy nail polish remover
         6      Buy nails

>提示这里面的6是相对行数，在文档中不是6  
>格式:[range]copy {address}  
>*命令*表

||Command ||Effect||
||:6t.  ||Copy line 6 to just below the current line||
||:t6 ||Copy the current line to just below line 6||
||:t.  ||Duplicate the current line (similar to Normal mode yyp )||
||:t$ ||Copy the current line to the end of the file||
||:'<,'>t0 ||Copy the visually selected lines to the start of the file||

>格式:[range]move {address}  

---

    original
    本文本参见上部分(copy部分)
<p>
    
    keystrokes
    鼠标{start}@Hardware的H上
`Vjj:m$`

    result

    Shopping list
        Beauty Parlor
            Buy nail polish remover
            Buy nails
        Hardware Store
            Buy nails
            Buy new hammer
    

**Tip30常用技巧:使用常规模式命令在选项范围内(Run Normal Mode Commands Across a Range)**

---
    original

var foo = 1
var bar = 'a'
var baz = 'z'
var foobar = foo + bar
var foobarbaz = foo + bar + baz

    keystrokes
`A;< Esc>jVjjjj:normal.`

    result

var foo = 1;  
var bar = 'a';  
var baz = 'z';  
var foobar = foo + bar;  
var foobarbaz = foo + bar + baz;  
>注:自行匹配行数，和相对行数

**Tip31 重复Ex命令(Repeat the Last Ex Command)**

看:h @:

**Tip32用Tab补全你的Ex命令(Tab-Complete Your Ex Commands)**

---用IDE的同志们，这是常用技能 看 :h :command-complete
> 主动掷出列表
`:col< C-d>`  
`:colorscheme < C-d>`

**Tip33通过命令提示输入当前字母(Insert the Current Word at the Command Prompt)**

---

    original 
var tally;  
for (tally=1; tally <= 10; tally++) {  
    // do something with tally  
};  

    keystrokes
    鼠标{start}@第一行的tally t上面
`*cwcounter< Esc>`  
`%s//< C-r>< C-w>/g`

var counter;  
for (counter=1; counter <= 10; counter++) {  
    // do something with counter  
};  

**回忆命令历史(Recall Commands from history)**
>:打头，<up><down>能够展示历史命令  
>/打头，<up><down>能够展示搜索历史  
>同样为了不离开主编辑区，可以使用< C-p>/< C-n>替代  

>组合命令使用|而非 bash里面的&& 比如 `:write |! ruby % 

> 当然你也可以使用 `q:`来像Insert mode一样编辑历史命令.

*进入cli-win的方式*表

||q/ ||Open the command-line window with history of searches||
||q: ||Open the command-line window with history of Ex commands||
||ctrl-f ||Switch from Command-Line mode to the command-line window||
