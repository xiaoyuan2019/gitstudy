## Git：版本控制系统

## 一、示意图

![1568079388406](C:\Users\Administrator.USER-20190313EO\AppData\Roaming\Typora\typora-user-images\1568079388406.png)

说明：

1.Workspace：工作区，即平时开发写代码的地方，比如IDE等开发工具，未受git管理；

2.Index：暂存区(索引区)，通过git add命令添加文件进来受git监控与管理；

3.Repository：本地仓库，通过git commit命令提交文件进来；

4.Remote：远程仓库、git服务器，通过git push命令将本地仓库文件推送到远程仓库进行同步，保持一致；



## 二、基本命令

#### 1.git init

新建空文件夹gitstudy，并进入该文件夹运行命令：git init，如下图所示：

![1568079884510](C:\Users\Administrator.USER-20190313EO\AppData\Roaming\Typora\typora-user-images\1568079884510.png)

​        执行命令后，会提示初始化空的git版本仓库，并自动生成一个隐藏文件夹.git，包含git的各种配置文件和依赖环境，不懂git的同学，务必不要随意更改此文件夹中的任何内容。

​        现在，文件夹gitstudy已经是一个本地git仓库了。。。



#### 2.git config --global

在开始正式使用git之前，务必先自报家门，使用命令git config --global user.name "xiao yuan"和git config --global user.email "yuan.xiao@mail.foxconn.com"，这样以后在每次提交文件至本地仓库时，都会带上这个消息，在我们排错、提交、回退等操作的时候，会清楚看到是谁提交的。



#### 3.git status 

使用命令：git status 查看工作区状态，有没有文件、文件有没有被跟踪、文件有没有被修改等等，如下图所示：

![1568080074303](C:\Users\Administrator.USER-20190313EO\AppData\Roaming\Typora\typora-user-images\1568080074303.png)

​         可以看到，没有任何可以提交的文件，提示要先创建或复制文件并且使用命令add进行跟踪，下面创建新的文件1.html。

​         git status -s：可以让输出更简洁明了。

![1568086235669](C:\Users\Administrator.USER-20190313EO\AppData\Roaming\Typora\typora-user-images\1568086235669.png)



#### 4.git add

创建空文件1.html，并加入git跟踪与管理，使用命令：git add 文件名，如下图所示：

![1568080595113](C:\Users\Administrator.USER-20190313EO\AppData\Roaming\Typora\typora-user-images\1568080595113.png)

​           使用git status可以看到文件1.html已经成功加入到暂存区受git跟踪了，这里的跟踪是指文件状态跟踪，如下图所示：

![1568080696967](C:\Users\Administrator.USER-20190313EO\AppData\Roaming\Typora\typora-user-images\1568080696967.png)

untracked：文件还在工作区，未添加进暂存区，未使用命令add；

unmodified： 文件已经通过add添加进暂存区，而且没有修改过该文件；

modified： 文件被修改过，但未添加进暂存区；

staged：文件被加入暂存区；

通过git commit命令将暂存区文件提交至本地仓库，同时删除暂存区文件。



#### 5.git commit

使用命令git commit可以将暂存区文件提交至本地仓库，参数-m对此次文件提交作文字说明，作为负责任的程序员，这个必须加上，这样在排错、回退的时候，可以知道这个文件修改了什么。

![1568082585134](C:\Users\Administrator.USER-20190313EO\AppData\Roaming\Typora\typora-user-images\1568082585134.png)

​          commit之前没有设置用户名和邮箱，所以默认设置了root，可以使用参数--reset-author重新设置。此时暂存区文件1.html已经被保存进本地仓库了。



#### 6.git log

使用命令git log可以查看详细的提交事件，包括版本号、作者、时间、描述，如下图所示：

![1568082776917](C:\Users\Administrator.USER-20190313EO\AppData\Roaming\Typora\typora-user-images\1568082776917.png)

版本号是唯一的，后面可以用于回退和跳转。



#### 7.git reflog

使用命令git reflog可以查看到所有历史事件，包含各种回退和跳转。

![1568087643844](C:\Users\Administrator.USER-20190313EO\AppData\Roaming\Typora\typora-user-images\1568087643844.png)

`[root@localhost gitstudy]# git reflog`
`3377df6 HEAD@{0}: reset: moving to HEAD^`
`978c592 HEAD@{1}: commit: add h5 tag,changed tag 3 and tag 4`
`3377df6 HEAD@{2}: commit: add h4 tag`
`bcf98bd HEAD@{3}: commit: add h3 tag`
`c6d661d HEAD@{4}: commit (initial): add empty html file`

#### 8.git log --pretty=oneline

该命令可以以单行打印的简略信息展现出操作记录

![1568093566619](C:\Users\Administrator.USER-20190313EO\AppData\Roaming\Typora\typora-user-images\1568093566619.png)



#### 9.git diff filename

使用该命令可以查看工作区和暂存区的文件内容区别，比如a.html文件之前已经add进暂存区了，后来修改了这个文件内容，但没有执行add命令。

![1568086983661](C:\Users\Administrator.USER-20190313EO\AppData\Roaming\Typora\typora-user-images\1568086983661.png)

再次执行add命令，将修改后的文件加入暂存区，然后使用git diff查看文件区别，结果显示没区别，说明工作区文件的修改已经同步到暂存区了。

#### 10.git diff --cached filename

该命令用于查看暂存区和本地仓库最新版本的文件区别，一旦文件从暂存区commit到仓库后，那么暂存区和本地仓库中的文件是没有任何区别的；如果文件没有commit，那么暂存区跟本地仓库中的文件是有区别的。

#### 11.git diff HEAD filename

使用该命令可以查看工作区文件和本地仓库最新版本文件的内容差别，比如修改后的a.html还没用add进暂存区，使用该命令查看本地仓库中的a.html与工作区的a.html有何差别。

![1568087166555](C:\Users\Administrator.USER-20190313EO\AppData\Roaming\Typora\typora-user-images\1568087166555.png)

执行commit命令，将暂存区的文件a.html提交至本地仓库，然后执行命令git diff HEAD查看两者区别，结果显示无区别，说明已经将暂存区文件同步到本地仓库了。

**这里的HEAD表示指针，指向的是本地仓库中最新的一个版本。**

## 三、回退与跳转

对html文件做三次修改三次提交，来测试版本回退和跳转。

![1568086701396](C:\Users\Administrator.USER-20190313EO\AppData\Roaming\Typora\typora-user-images\1568086701396.png)

这是第一次修改，后面两次随便添加东西即可。修改完后，使用命令git log查看所有提交的事件。

#### 1.修改事件准备

![1568087579283](C:\Users\Administrator.USER-20190313EO\AppData\Roaming\Typora\typora-user-images\1568087579283.png)



#### 2.回退到上一个版本：git reset --hard [HEAD^|版本号]

HEAD表示指针，^表示回退一次，即上一次修改状态，我们执行一下这个命令，如下所示：

![1568094002390](C:\Users\Administrator.USER-20190313EO\AppData\Roaming\Typora\typora-user-images\1568094002390.png)

当要回退到以前第10个版本时，我们不可能在HEAD后面加10个^，因此，有另外一种办法可以直接回退到任一版本，就是--hard后面加事件的版本号(建议写完整的版本号，前6位也行，不过事件多的时候可能会重复)。如git reset --hard bcf98b

#### 3.回退到最新版本：git reset --hard 版本号

由于之前回退到旧版本后，命令git log显示不出最新版本的版本号，根据这条命令的输出我们无法回到最新版本中。此时，有另外一条命令可以查看到所有事件的版本号，就是git reflog，如下图所示：

![1568094560509](C:\Users\Administrator.USER-20190313EO\AppData\Roaming\Typora\typora-user-images\1568094560509.png)

这个命令的输出会显示所有操作的事件信息，如要回到最新版本事件，那么只需要找到它的版本号即可。

执行命令：git reset --hard 978c592回退到最新版本

![1568098658007](C:\Users\Administrator.USER-20190313EO\AppData\Roaming\Typora\typora-user-images\1568098658007.png)



## 四、高级命令

#### 1.撤销操作：git checkout -- | git reset HEAD filename

**撤销情景一：工作区文件被修改且没有执行add+commit操作。**

此时执行命令git status其实已经显示了如何撤销修改了，如图所示：

![1568101082594](C:\Users\Administrator.USER-20190313EO\AppData\Roaming\Typora\typora-user-images\1568101082594.png)

执行命令：git checkout -- b.md，结果如下：

![1568101253206](C:\Users\Administrator.USER-20190313EO\AppData\Roaming\Typora\typora-user-images\1568101253206.png)

**撤销情景二：工作区文件被修改且执行add操作但没commit。**

如下图所示：提示使用命令git reset HEAD filename可以撤销已经加入暂存区的文件修改。

![1568102069336](C:\Users\Administrator.USER-20190313EO\AppData\Roaming\Typora\typora-user-images\1568102069336.png)

执行命令：git reset HEAD b.md，可以将文件撤销到未加入暂存区，如下图所示：

![1568102258388](C:\Users\Administrator.USER-20190313EO\AppData\Roaming\Typora\typora-user-images\1568102258388.png)

此时文件跟情景一一致了，然后使用命令git checkout -- b.md可彻底撤销。



#### 2.删除操作：特殊的修改撤销操作

删除文件a.html进行测试，可以看到当前工作区的状态，因为文件已经在本地仓库中，删除后工作区和本地仓库文件状态不同步，需要同步到本地仓库。此时可以通过命令git diff和git diff HEAD查看文件区别。

![1568107425072](C:\Users\Administrator.USER-20190313EO\AppData\Roaming\Typora\typora-user-images\1568107425072.png)

删除操作还未同步到暂存区，如果要撤销删除操作，使用git checkout -- a.html即可，如下图所示，删掉的文件a.html又回来了。

![1568107859810](C:\Users\Administrator.USER-20190313EO\AppData\Roaming\Typora\typora-user-images\1568107859810.png)

要想继续删除文件，将信息从暂存区同步到本地仓库，根据提示信息，执行同步删除操作的命令：git rm a.html，此时要删除的文件不在工作区和暂存区了，继续执行commit命令，即可删除本地仓库中的文件a.html。

![1568159253865](C:\Users\Administrator.USER-20190313EO\AppData\Roaming\Typora\typora-user-images\1568159253865.png)

如果此时又不想删除文件了，可以使用命令：git reset HEAD a.html将文件恢复到暂存区，然后再执行：git checkout -- a.html恢复到工作区即可。跟撤销修改操作是一样的，分两步恢复。

**注意：**

**1.如果你确实要删除，那么直接rm + git rm + git commit即可，如果你后悔了，想让它回来，版本回退即可。**

**2.如果先创造文件再删除文件，这时的暂存区与版本库是没有你创造的那个文件的，遇到这种情况，格外注意一下即可。**



## 五、Git工作原理

#### 1.概念

Git与集中式版本管理系统不同的是，多了个暂存区的概念，也正是因为这个暂存区的概念，Git逻辑清晰，功能强大，成为了最先进的分布式版本控制系统。

先来看看工作区的概念，所谓工作区就是learngit文件夹，是经过git init配置好的git仓库

我们知道，配置git仓库的时候，产生了一个.git的隐藏目录，这儿是Git的版本库

在这个.git版本库里面最重要的概念就是暂存区，可以称作为stage（或index）

![1568097660928](C:\python项目备份\备份20190823\gitstudy\img\1568097660928.png)

所以我们的add+commit的详细流程到底是什么？如上图所示：

就是我在工作区的时候创建或修改了文件或文件夹，然后使用add命令的时候，将文件或文件夹加入暂存区，再使用commit提交的时候，将暂存区的所有内容正式同步到当前master的分支Git仓库，产生了新的版本号，HEAD指针向上移动指向了新的版本号，完成Git仓库内容的更新。

#### 2.git diff总结

我们在工作区改动文件、添加到暂存区，提交到版本库这三个阶段走来，git diff总能发挥出对比状态的作用

①git diff filename：比较文件在工作区与暂存区的变化（在工作区改动文件，还未add+commit）

②git diff --cache filename：比较文件暂存区与当前版本库的变化（已经将文件添加进去暂存区，但还未提交）

③git diff HEAD filename：比较工作区与当前版本库的变化（说白了，就是看你的改动还没被commit）



#### 3.撤销修改和删除操作总结

说实话，其实修改与删除都属于"修改"，操作没有本质区别，所以我将这两个放到一起总结

①当你在工作区修改或删除的时候，想要撤销，统一git checkout -- filename（两个横杠不能省略）

②当你的修改或删除真的要确定的话，进一步git add/rm，然后commit上去。如果你执行了加入暂存区过后，你后悔了，想要撤销就git reset HEAD filename，将暂存区的变动回退。当然了，你还可以进一步地git checkout -- filename直接回到最初的状态，装作无事发生。

③当你的修改或删除，都走了add+commit的步骤，这个时候直接版本回退即可。



## 六、本地仓库和GitHub仓库互访

##### 1.本地仓库生成ssh公钥

![1570153827408](img\1570153827408.png)

##### 2.登录GitHub，新建ssh key

如下图所示：

![1570155488421](img\1570155488421.png)

点击右边的  New SSH key，把刚才在本地仓库生成的ssh 公钥 内容复制进去保存即可。

![1570156194036](img\1570156194036.png)

![1570156270406](img\1570156270406.png)

完成后，可看到如下界面：

![1570156596681](img\1570156596681.png)

至此，本地仓库和GitHub远程仓库可互相连接了。。。
