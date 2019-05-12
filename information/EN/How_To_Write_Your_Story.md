# Operation Miskatonic Instruction Document
## Written by Bob Guo

# WARNING
Due to the maintainer of this project uses Chinese as his/her mother language, Chinese version of the instruction files should be consider as what the maintainer wants to express.
The maintainer have done all he/she can do to make Chinese version and English version as similar as possible. So if you have ever found any mistakes, please email to boblao0714@gmail.com or report a issue.  
***

## How-To write your own story
The story file is at "story", you should put your image and audio in order and write script in such order:  
> [player.Charactor]"This is a strange subject", [san] (Test_1)  
> [npc.Charactor]"This is not what it should look like" [knowledge] (Test_1)    
> [game.Subject]"This item gives people a strange feel" [san] (Test_1)  

The first parentheses shows what kind of object is saying. In my project, the engine could understand script sentense start with [xxx,xxx]. First xxx means what kind of object it is. It is either player,or NPC or just keeper. The later "Charactor" or "Subject" is where you should write down the name of the subject. If the parentheses says [game.GAME], then the phrase IS from the game itself and it usually means something happened and led to some results.  

The latter shows what kind of event should be running after this sentense. In COC, events usually comes with ending either lose or add some points to a player character's card. You should change Test_1 to whatever you wrote and the parentheses in front means the name of the data that is either losing or adding. This engine should be able to understand everything from COC rulebook Ver.7 like SAN.  

More information about how to write the story can be found in later updates in master branch of the repo. 


# CREATOR
THIS IS A POLARIS CLUB PROJECT  

Join us : boblao0714@gmail.com  