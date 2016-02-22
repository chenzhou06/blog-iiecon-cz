Title: My First Emacs Package
Author: Chen Zhou
Date: 2016-02-21 16:54
Category: Programming
Tags: programming, elisp, emacs

When I am about initializing a new project, a `README` file should be added for
the future uploading to GitHub. Editing Markdown is not convenient once one
wants to tune the output frequently. There are a few packages available in Melpa,
but non of those fully take advantage of GitHub's API to render the `README`
file as it should look like on the repository's front page. Finally, Google
tells me that there is an excellent application written in python, which can
take care of a git repository and render Markdown files in
[GitHub Flavored Markdown](https://guides.github.com/features/mastering-markdown/#GitHub-flavored-markdown)
mode with real-time preview supporting.

My first package for Emacs provides a minor mode which can start a process where
Grip works in the background rendering files. The essential part of this package
utilizes the function `start-process-shell-command` which starts a program in a
subprocess, creates a buffer associated with that subprocess.

The macro `define-minor-mode` also facilitates the development procedure. All I
have to do is writing a function invoking `start-process-shell-command`, then
passing it to the macro's body.

For the time being, this package looks like this:

```elisp
(defgroup markdown-grip-mode nil
  "Realtime Markdown previews via grip."
  :group 'markdown-grip
  :prefix "markdown-grip-")

(defcustom markdown-grip-port 6419
  "Port on which grip server will run."
  :type 'integer
  :group 'markdown-grip)

(defcustom markdown-grip-open t
  "Open browser automatically."
  :type 'boolean
  :group 'markdown-grip)

(defconst grip-process-name "Grip-process"
  "Name for grip process.")
(defconst grip-buffer-name "*Grip*")

(defun markdown-grip-run ()
  "Preview the current buffer using grip."
  (interactive)

  (unless (executable-find "grip")
	  (error "Grip is not in `exec-path'"))

  (start-process-shell-command
   grip-process-name
   grip-buffer-name
   (format "grip %s %s %s"
	   (if markdown-grip-open "-b" "")
	   buffer-file-name
	   markdown-grip-port))

  (print (format "%s rendered @ %s"
		 buffer-file-name
		 markdown-grip-port)
	 (get-buffer "*Grip*")))

(defun markdown-grip-stop ()
  "Stop the grip process."
  (interactive)
  (if (buffer-live-p grip-buffer-name)
	  (kill-buffer grip-buffer-name))
  (if (process-live-p grip-process-name)
	  (quit-process grip-process-name)))

(define-minor-mode markdown-grip-mode
  "Realtime preview mardown with grip."
  :lighter " Grip"
  (if (bound-and-true-p markdown-grip-mode)
	  (markdown-grip-run)
	(markdown-grip-stop)))

(provide 'markdown-grip-mode)
```
