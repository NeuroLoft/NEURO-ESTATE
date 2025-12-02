cd /d "c:\Users\admin\Desktop\Проект РП\Release"
echo START > debug.txt
git config core.editor echo
git merge --abort
git pull origin main
git push origin main > push_log.txt 2>&1
echo END >> debug.txt