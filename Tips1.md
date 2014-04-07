**Tip52删除周遭,或者更新内部(Delete Around ,or Change Inside)**

>*Text Objects*表

||Keystrokes ||Buffer Contents||
||iw ||Current word||
||aw ||Current word plus one space||
||iW ||Current WORD||
||aW ||Current WORD plus one space||
||is ||Current sentence||
||as ||Current sentence plus one space||
||ip ||Current paragraph||
||ap ||Current paragraph plus one blank line||

---

    original
Improve your writing by deleting excellent adjectives.

    keystrokes
    鼠标{start}@excellent 的x字母上
`daw`
    
    result

    Improve your writing by deleting adjectives.

--- 
    original
Improve your writing by deleting excellent adjectives.

    keystrokes
    鼠标{start}@excellent 的x字母上
`ciwmost< Esc>`

    result

    Improve your writing by deleting most adjectives.

>同样可以把iw,换成Tip52里面的所以{motion}


**Tip53虽然不能翻译但是这节讲标记以供快速Jump(MarkYourPlaceandSnapBackto)It**
>请查看`:h m`

>`m{a-zA-Z}`能够定义多个 marker，以供`'{a-zA-Z}`使用.  
>当然vim还有部分*automatic Marks*的表

 ||Keystrokes ||Buffer Contents||
 ||`` ||Position before the last jump within current file||
 ||`.  ||Location of last change||
 ||`^ ||Location of last insertion||
 ||`[ ||Start of last change or yank||
 ||`] ||End of last change or yank||
 ||`< ||Start of last visual selection||
 ||`> ||End of last visual selection||


**Tip 54在匹配的对应子集跳转(Jump Between Matching Parentheses)**
>本节主角是`%`

---
>一些操作实效

||Keystrokes ||Buffer Contents||
||{start} ||console.log([{'a':1},{'b':2}])||
||||__________x_______________||
||% ||console.log([{'a':1},{'b':2}])||
||||_________________________x||
||h ||console.log([{'a':1},{'b':2}])||
||||________________________x_||
||% ||console.log([{'a':1},{'b':2}])||
||  ||___________x______________||
||l ||console.log([{'a':1},{'b':2}])||
||  ||____________x_____________||
||% ||console.log([{'a':1},{'b':2}])||
||  ||_________________x________||

>注:x为光标位置 



---
>一些操作实效

||Keystrokes ||Buffer Contents||
||{start} ||cities = %w{London Berlin New\ York}||
||        ||________x___________________________||
||dt{ ||cities = {London Berlin New\ York}||
||        ||________x___________________________||
||% ||cities = {London Berlin New\ York}||
||        ||_______________________________x____||
||r] ||cities = {London Berlin New\ York]||
||        ||_______________________________x____||
||`` ||cities = {London Berlin New\ York]||
||        ||_______x____________________________||
||r[ ||cities = [London Berlin New\ York]||
||        ||____________________________________||

>提示`  ``  `命令要配合< C-o>  
>可查看*Tip13*    

**游戈于Jump List(Traverse the Jump List)**
>`:jumps`大概你能看到一个列表表示你到过哪里，  
>可以通过< C-o>与< C-i>来切换游走  
>当然有个*快捷键*表

||Command ||Effect||
||[count]G ||Jump to line number||
||//pattern <CR> /?pattern <CR> / n / N ||Jump to next/previous occurrence of pattern||
||% ||Jump to matching parenthesis||
||( / ) ||Jump to start of previous/next sentence||
||{ / } ||Jump to start of previous/next paragraph||
||H / M / L ||Jump to top/middle/bottom of screen||
||gf ||Jump to file name under the cursor||
||<C-]> ||Jump to definition of keyword under the cursor||
||’{mark} / `{mark} ||Jump to a mark||

**Tip56在Change List上跳转(Traverse The Change List)**
>`:changes`大概你还能看到一个列表表示你的更新过哪里，  
>同样这次你可以用`g;或g,`

**Tip57可能通过文件名来跳转(Jump to the Filename Under the Curser)**
>这个理解比较简单    
>首先(使用之前的技能`!touch /tmp/test.t`然后在当前文本中输入  
>/tmp/test.t  
>操作之前请保存，不然你会迷失的  

**Tip58使用全局Marks(Snap Between Files Using Global Marks)**
>基本上就是`m{letter}`里面的大小写的关系，用大写字母就像使用书签一样  
>可以在文件中跳转  
>请自行演示，问题请google或call me

**Tip59删除,抽取,和推送通过vim's没有命令的注册列表(Delete, Yank, and Put with Vim’s Unnamed Register)**

---

||Keystrokes ||Buffer Contents||
||{start} ||Practica lvim||
||        ||___________x||
||F␣ ||Practica lvim||
||        ||_______x____||
||x ||Practicalvim||
||        ||_______x____||
||p ||Practical vim||
||        ||________x___||

>提示:x为水标位置，而且假如你看到F后面一个方框说明你不能显示  
>某些字符，解决方法很简单看穿尘世，  

||Keystrokes ||Buffer Contents||
||{start} ||2) line two||
||        ||x__________||
||   ||1) line one||
||   ||3) line three||
||dd   ||1) line one||
||   ||3) line three||
||pp   ||1) line one||
||   ||2) line two||
||   ||3) line three||

>能看懂吗？要尝试的话也直接通过以上文本实现，  
>也可以自行意念理解下  


**Tip60Grok Vim’s Registers**
>讲的好复杂，大意是说了些能够register的操作  
>比如`x,s,d{motion},c{motion},y{motion}`  
>可以`:reg "0`  

**Tip61用注册器替换选项区(Replace a Visual Selection with a Register)**

---
    original
collection = getCollection();  
process(somethingInTheWay, target);  

    keystrokes
`yiwjwwvep`

    result
    collection = getCollection();
    process(collection, target);


---
    original

I like chips and fish.

    keystrokes
fcdemmwwvep`mP

>提示这儿没有代码块是因为我还不知道怎么在代码块中显示`,我也没Google在边上  


    result

    I like fish and chips.

**Tip62从Register中粘贴(Paste from a Register)**

--- 
    original
collection = getCollection();  
process(somethingInTheWay, target);  

    keystrokes
`yiwjwwciw< C-r>0< Esc>`

    result

collection = getCollection();  
process(collection, target);  

---
    original

    <table>
        <tr>
            <td>Keystrokes</td>
            <td>Buffer Contents</td>
        </tr>
    </table>

<p>

    keystrokes
`/<tr>yapgP`

    result

    <table>
        <tr>
            <td>Keystrokes</td>
            <td>Buffer Contents</td>
        </tr>
    </table>

    <table>
        <tr>
            <td>Keystrokes</td>
            <td>Buffer Contents</td>
        </tr>
    </table>

>如果你得到了一个table，请不要在意这些细节要看破红尘。因为你的vim  
>识别的段落不一致。  

**Tip63联系系统剪切板(Interact with the System Clipboard)**
>大概的意思是让你明白` :set pastetoggle=<f5> `
>请自行Google pastetoggle。上面讲的比这清楚或者例子  
> 不能很好展现 

**Tip64录制和执行一个宏(Record and Execute a Macro)**
>这节开始我们就要练习宏了，和office的宏一样  
>就是一组操作的集合  

---
    original
foo = 1
bar = 'a'
foobar = foo + bar


    keystrokes
`qaA;< Esc>Ivar < Esc>q`

    result

    var foo = 1;
    bar = 'a'
    foobar = foo + bar

>在这里不能只看到最后效果，  
>请运行`:reg a`
>你应该能看到如下

    :reg a
    --- Registers ---
    "a   A;^[Ivar ^[
    Press ENTER or type command to continue

>没错我们录制了宏，开始执行吧，

---
    original

var foo = 1;  
bar = 'a'  
foobar = foo + bar  

    keystrokes
    鼠标{start}@var后面的空格上
`j@aj@@`

    result

    var foo = 1;  
    var bar = 'a'  ;
    var foobar = foo + bar  ;

>以上说明执行可以用@a 和@@来，@a可以区分不同的宏  
>而@@则可以快速执行上个录制的宏  


**Tip65Normalize, Strike, Abort**
>TODO
>无


**Tip66 执行次数 (Play Back with a Count)**

---
    original
x = "("+a+","+b+","+c+","+d+","+e+")";

    keystrokes
    这次我们录制一个q的macro并执行了22次
`f+s + < Esc>qq;.q22@q`
        
    result

x = "(" + a + "," + b + "," + c + "," + d + "," + e + ")";

>是不是很神奇。

**Tip67Repeat a Change on Contiguous Lines**

---

    original
1. one  
2. two  

    keystrokes
    光标{start}@one的o上面
`qa0f.r)w~jq`


1) One  
2. two  

>可以看`:reg a`

    :reg a
    --- Registers ---
    "a   0f.r)w~j
    Press ENTER or type command to continue


>这次我们要使用以上录制的宏

---
    original
    
1) One  
2. two  
3. three  
4. four  

    keystrokes
    光标{start}@two的w上面
`3@a`


    result

    1) One  
    2) Two  
    3) Three  
    4) Four  

>bingo没让你失望吧，下面请看碰到异常怎么继续  

---
    original

1. one
2. two
// break up the monotony
3. three
4. four

<p>

    keystrokes
`使用以上录制的宏`  
`5@a`

    result

    1) One
    2) Two
    // break up the monotony
    3. three
    4. four

>结果卡住了
>没关系 我们要并行的执行宏来消除这个



---
    original

1. one
2. two
// break up the monotony
3. three
4. four

<p>

    keystrokes
    `使用以上录制的宏`  
`VG:normal @a`    

    result

    1) One
    2) Two
    // break up the monotony
    3) Three
    4) Four

>`VG`请自行调整选中区域到第1到第5 

**Tip68追加宏脚本(Append Commands to a Macro)**

>这节意思相当简单就是`q{letter}`会overwrite一个宏  
>但你用了`q大写字母时`就会在后面追加命令  

**Tip69(Act Upon a Collection of Files)**
>TODO
>无
>请自行演示  

**Tip70(EvaluateanIteratortoNumberItems in a List)**

---
    original
partridge in a   
French hens  
calling birds  
golden rings  
tree  

    keystrokes
`let i=1`        #初设置i  
`qaI< C-r>=i<CR>)< Esc>`    
`let i +=1`   #加1  
`q`  #结束录制  
` jVG`    #同理请自行调整`VG`或者独立文件运行演示  
`:normal @a`  

    
    result

1)partridge in a   
2)French hens  
3)calling birds  
4)golden rings  
5)tree  

>提示演示不通过请call me


**Tip71编辑宏**
>此章节和编辑替换一样，自行演示或交流，文档不好展示

**Tip72调整大小写搜索模式(Tune the Case Sensitivity of Search Patterns)**
>此节意思明了，用\c来忽略大小匹配   
>当然你也能用`:set ignorecase`来全局忽略大小写匹配  

**Tip73,74**
>使用\v来匹配正则式  
>关于正则是门大学问，我不想糟蹋了这个精华，请专门阅读正则大作  

**Tip75用模式匹配(UseParenthesestoCaptureSubmatches)**

----
    original
I love Paris in the  
the springtime.  

    keystrokes
`/\v<(\w+)\_s+\1>`
 
    result
    是不是很神奇的匹配了the the 
    算了我又在亵渎神圣的正则请自行google

**Tips76,77,78这几单都是讲搜索正则的**
>Pass
>真不想译，请GOOGLE


**Tip79初见搜索模式(Meet the Search Command)**

||Command ||Effect||
||n ||Jump to next match, preserving direction and offset||
||N ||Jump to previous match, preserving direction and offset||
||/ <CR> ||Jump forward to next match of same pattern||
||? <CR> ||Jump backward to previous match of same pattern||

>一切在不言中，搜索历史的话使用< up>< down>

**Tip80,81讲更友好的搜索选项**
>其实涉及一些 .vimrc的配置
>如下

    set hlsearch spell 
    set incsearch  
    set is        
    set smartcase 

**Tip82计算匹配的模式(Count the Matches for the Current Pattern)**
>两种方法  
>方法1   
` :%s///gn `  
>方法2  
` :%s//&/g `  

>大概第一种比较好，因为不会触发编辑

**Tip83定位到模式末位 (Offset the Cursor to the End of a Search Match)**


---
    original
Aim to learn a new programming lang each year.  
Which lang did you pick up last year?  
Which langs would you like to learn?  

    keystrokes
`/lang/e< CR>auage< Esc>n.n.`

    result


    Aim to learn a new programming language each year.  
    Which language did you pick up last year?  
    Which languages would you like to learn?  

>匹配完模式后加`/e`


**Tip84一个完整的匹配搜索(Operate on a Complete Search Match)**


---
    original

class XhtmlDocument < XmlDocument; end
class XhtmlTag < XmlTag; end

    keystrokes
`/\vX(ht)?ml\C< CR>gU//e< CR>//< CR>.//< CR> .`

    result


    class XHTMLDocument < XMLDocument; end
    class XHTMLTag < XmlTag; end

**Tip85创建一个复杂的模式(CreateComplexPatternsbyIterating uponSearch History)**

>看例子

---
    original
This string contains a 'quoted' word.  
This string contains 'two' quoted 'words.'  
This 'string doesn't make things easy.'  

    keystrokes
1.`/\v'[^']+'`    
2.` /\v'([^']|'\w)+'`  
3.`/\v'([^']|'\w)+'`  

    result

    请自行查看三种搜索的结果

**Tip86Visual Selection也可以使用搜索(SearchfortheCurrentVisualSelection)**

||Keystrokes ||Buffer Contents||
||{start} ||She sells sea shells by the sea shore.||
||        ||xxxxxxxxxxxx__________________________||
||* ||She sells sea shells by the sea shore.||
||        ||xxxxxxxxxxxxxxxxxxxxxxxxxx____________||

>提示x表示选中区域
