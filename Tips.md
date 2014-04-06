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
