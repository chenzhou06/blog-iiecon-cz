Title: Table to CSV in Org-Mode
Author: Chen Zhou
Category: Programming
Tags:  emacs
Date: 2016-04-22 17:38:54

Today I have a trivial task which requires me to transform several lines of
number-name pairs to a csv dataset. I can do it by hand but I am reluctant to
resort to stupid repeating since I know a little programming.

The source text looks like this:

	11 北京 12 天津 13 河北 14 山西 15 内蒙古 21 辽宁 22 吉林 23 黑龙江 31 上海 32 江苏 33 浙江 34 安徽
	35 福建 36 江西 37 山东 41 河南 42 湖北 43 湖南 44 广东 45 广西 46 海南 50 重庆 51 四川 52 贵州
	53 云南 54 西藏 61 陕西 62 甘肃 63 青海 64 宁夏 65 新疆

My task is to rearrange this text line by line and insert a comma between every
pair of number and name. The desired result looks like this:

	11,北京
	12,天津
	13,河北
	14,山西
	15,内蒙古
	21,辽宁
	...

The first thought occurred to me is writing a program which takes a pair of
number and name from an input stream and transform them into a csv file. I quit
this thought very soon because it involves too much over head. The final
solution I chose is that using `replace-regexp` in Emacs to insert a `\n` before
every number, then using `C-c |` in `org-mode` to convert it to a table which in
the end can be exported as a csv file with `org-table-export`.

Many unexpected troubles happened when I was using `replace-regexp`. I had to
capture every number which is actually two digits, and replace it with a "\n"
and the content being captured. To capture two digits, I used regexp
`\([[:digit:]][[:digit:]]\)` which is very cumbersome compared with `\d{2}` in
Perl. The most difficult thing which cost me much of my time is entering a
newline character in the `minibuffer`. I tried "\n", "\\n" but all
failed. Finally, I finally figured out I have to enter `C-c q C-c j` to insert a
newline. Can this be more redundant?

Emacs lisp provides `\&` to represent the captured content in the object text
replacing the matched text. After this procedure, my source text became like this:

	11 北京
	12 天津
	13 河北
	14 山西
	...

At this stage, `C-c |` in `org-mode` transforms it to a table which can be
exported as a csv file using `org-table-export`.
