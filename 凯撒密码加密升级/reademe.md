要求如下：

***\*Design work\**** ***\*1：\*******\*Simulation\**** ***\*software\**** ***\*Implementation of upgraded Caesar encryption algorithm\****

1. The interface of the designed decryption software of Caesars upgraded version is shown in the figure: （注意映射表第一行要设置成不能修改状态，只能修改映射表的第二行）

![img](file:////Users/m1st/Library/Containers/com.kingsoft.wpsoffice.mac.global/Data/tmp/wps-m1st/ksohtml//wps1.png)![img](file:////Users/m1st/Library/Containers/com.kingsoft.wpsoffice.mac.global/Data/tmp/wps-m1st/ksohtml//wps2.png) 

![img](file:////Users/m1st/Library/Containers/com.kingsoft.wpsoffice.mac.global/Data/tmp/wps-m1st/ksohtml//wps3.png)![img](file:////Users/m1st/Library/Containers/com.kingsoft.wpsoffice.mac.global/Data/tmp/wps-m1st/ksohtml//wps4.png)![img](file:////Users/m1st/Library/Containers/com.kingsoft.wpsoffice.mac.global/Data/tmp/wps-m1st/ksohtml//wps5.jpg)

 

2. The operation is as follows: click the "load ciphertext file" button, load the zxwcipher.txt (this file has been given to everyone).

![img](file:////Users/m1st/Library/Containers/com.kingsoft.wpsoffice.mac.global/Data/tmp/wps-m1st/ksohtml//wps6.jpg)

Then click the "***\*decryp\*******\*t\****" button to see if the plaintext is correct or wrong

 

![img](file:////Users/m1st/Library/Containers/com.kingsoft.wpsoffice.mac.global/Data/tmp/wps-m1st/ksohtml//wps7.jpg)

 

 If you feel that the translated plaintext is incorrect, it means that the second line in the letter mapping table is set incorrectly. Please ***\*modify the second\**** ***\*line\**** ***\*of\**** ***\*letter mapping table\****, and click the "Decrypt" button again until the decrypted plaintext is correct. 

![img](file:////Users/m1st/Library/Containers/com.kingsoft.wpsoffice.mac.global/Data/tmp/wps-m1st/ksohtml//wps8.jpg)

 

 

At last, when you make sure the second line has been guessed correctly, you will get the key sentence. Finally, explain what the key sentence is, and make a literal theoretical analysis of your every step(给出密钥句子，并且对你的每一步做理论上的分析). 

The function of "Clear ciphertext" button is to clear the ciphertext text box.

3. The principle of the upgraded version of Caesars Password is as follows: 

An example is as below.

the plain text（明文）: I am in danger! 

The key sentence（密钥句子）: zhangsan.

The mapping relationship between lowercase plaintext letters and uppercase ciphertext letters is shown in Table 1, and the construction method is as follows: the first line of plaintext letters is filled with 26 letters written in order

The second line of ciphertext alphabetical order construction rules: first remove the duplicate letters in the key sentence (zhangsan), and then write it into the second line of the ciphertext alphabet, and then write the remaining letters of the 26 letters that are not used according to the letter table order.

Table 1 mapping table (plaintext is lowercase, the ciphertext is uppercase)

| Plaintext  | a           | b           | c           | d           | e           | f           | g    | h    | i    | j    | k    | l    | m    | n    | o    | p    | q    | r    | s    | t    | u    | v    | w    | x    | y    | z    |
| ---------- | ----------- | ----------- | ----------- | ----------- | ----------- | ----------- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| Ciphertext | ***\*Z\**** | ***\*H\**** | ***\*A\**** | ***\*N\**** | ***\*G\**** | ***\*S\**** | B    | C    | D    | E    | F    | I    | J    | K    | L    | M    | O    | P    | Q    | R    | T    | U    | V    | W    | X    | Y    |

|--- Key sentence ---|---The remaining letters of 26 lettersare written in alphabetical order --|

 

(plaintext is uppercase, the ciphertext is lowercase)

| Plaintext  | A           | B           | C           | D           | E           | F           | G    | H    | I    | J    | K    | L    | M    | N    | O    | P    | Q    | R    | S    | T    | U    | V    | W    | X    | Y    | Z    |
| ---------- | ----------- | ----------- | ----------- | ----------- | ----------- | ----------- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| Ciphertext | ***\*z\**** | ***\*h\**** | ***\*a\**** | ***\*n\**** | ***\*g\**** | ***\*s\**** | b    | c    | d    | e    | f    | i    | j    | k    | l    | m    | o    | p    | q    | r    | t    | u    | v    | w    | x    | y    |

|--- Key sentence ---|---The remaining letters of 26 lettersare written in alphabetical order --|

With the mapping table, then the text is ***\**I am in danger!\**\*** The ciphertext is ***\**d\**\*** ***\**ZJ\**\*** ***\**DK\**\*** ***\**NZKBGP\**\******\**!\**\*** 

Note: The mapping table in the maketrans function is the corresponding mapping table for all letters, including the mapping table for uppercase letters and the mapping table for lowercase letters.编程时候要2个映射表都要同时用到才能解密，但是软件界面上只需要写第一个映射表（小写字母abcd…xyz变成大写字母）

最终实现：

![image-20240626074930205](/Users/m1st/Library/Application Support/typora-user-images/image-20240626074930205.png)

![image-20240626075018630](/Users/m1st/Library/Application Support/typora-user-images/image-20240626075018630.png)

