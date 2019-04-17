
# Operation-Miskatonic

# WARNGING
Due to the maintainer of this project uses Chinese as his/her mother language, Chinese version of the README should be consider as what the maintainer wants to express.
The maintainer have done all he/she can do to make Chinese version and English version as similar as possible. So if you have ever found any mistakes, please email to boblao0714@gmail.com.  
  
## Project README  
A TRPG (Tabletop Role Playing Game) engine for single player work.  
This engine is a project of The Polaris Computer Club.  
According to our plan, this system SHOULD be able to support more than COC(Call of Cthulhu), but I DONT make any promises here.  
The game engine itself is open-sourced with MIT but the following materials are NOT, they include : Articles/Musics/Images and more.  
I plan to use Python as structure, and this game SHOULD be able to run on any system that supports Python 3. But as usual, I don't make any promise.   

### Features

IF everything goes right, after the project is done, I have two targets.  
Either re-write the engine in C or add multi-player mode  

### How-To write your own story
The story file is at "story", you should put your image and audio in order and write script in such order:  
> [player.Charactor]"This is a strange subject", [san] (Test_1)  
> [npc.Charactor]"This is not what it should look like" [knowledge] (Test_1)    
> [game.Subject]"This item gives people a strange feel" [san] (Test_1)  

The first parentheses shows what kind of object is saying. In my project, the engine could understand script sentense start with [xxx,xxx]. First xxx means what kind of object it is. It is either player,or NPC or just keeper. The later "Charactor" or "Subject" is where you should write down the name of the subject. If the parentheses says [game.GAME], then the phrase IS from the game itself and it usually means something happened and led to some results.  

The latter shows what kind of event should be running after this sentense. In COC, events usually comes with ending either lose or add some points to a player character's card. You should change Test_1 to whatever you wrote and the parentheses in front means the name of the data that is either losing or adding. This engine should be able to understand everything from COC rulebook Ver.7 like SAN.  

More information about how to write the story can be found in later updates in master branch of the repo.
## 项目说明
这个项目的目标是构建一个单人跑团TRPG 引擎。  
它是隔雨听竹的一个项目。  
我计划让这个引擎支持COC以外的游戏，但是我不做任何保证。根据我的最初计划，这个引擎是基于Python构建的，所以它应该能够在所有支持Python的系统上运行，但是我仍然不做任何保证。  
游戏引擎本体根据MIT协议开源，但是包括但不限于以下各项的内容并没有，请尊重我的工作：音乐/文章/图片等。  

### 计划

如果一切顺利，在这个引擎的基础搭建完成之后，关于这个项目的下一个目标要么是用C语言重写这个程序，要么就是增加一个多人游戏模式。  

### 如何自己写一个故事
故事文件被放在“story”文件夹里。在你故事相应的文件夹中，你需要把图片和音乐素材放到对应的文件夹中，脚本文件的写法应该是：
> [player.Charactor]"这个东西有点奇怪", [san] (Test_1)  
> [npc.Charactor]"这件事情不该如此" [knowledge] (Test_1)    
> [game.Subject]"这个物品给人一种奇怪的感觉" [san] (Test_1)  

第一个括号内的内容是指这句话的来源。这个项目中，引擎可以理解的脚本句式开头就是[xxx,xxx]。其中第一个xxx意味着这个来源的种类是什么。它要么是玩家角色，要么是NPC，要么就是守密人。之后的“Charactor”或者“Subject”应当被替换成对应的名称。如果这个括号中的内容是[game.GAME]，那么这句话的来源就是游戏本身，一般来讲，这种情况意味着发生了一些事情，然后造成了一些结果。  

句尾的标识显示的是游戏在这句话后需要做什么。根据克苏鲁的呼唤的说明，事件通常伴随着玩家角色某些点数的增减。你需要将“Test_1”更换成你想要程序做的事情，而这个“事情”一般指的就是对玩家角色的点数增减（a.k.a 骰子女神的微笑）。这个引擎应该能够理解所有第七版规则书中的点数代码。  

任何关于游戏自定义内容的修改请参照之后在本repo里更新的Instruction
# CREATOR
THIS IS A POLARIS CLUB PROJECT  

Join us : boblao0714@gmail.com  



<a href="https://996.icu"><img src="https://img.shields.io/badge/link-996.icu-red.svg" alt="996.icu" /></a>  