{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "3e7f5ae4",
   "metadata": {},
   "outputs": [
    {
     "ename": "ModuleNotFoundError",
     "evalue": "No module named 'requests'",
     "output_type": "error",
     "traceback": [
      "\u001b[31m---------------------------------------------------------------------------\u001b[39m",
      "\u001b[31mModuleNotFoundError\u001b[39m                       Traceback (most recent call last)",
      "\u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[3]\u001b[39m\u001b[32m, line 1\u001b[39m\n\u001b[32m----> \u001b[39m\u001b[32m1\u001b[39m \u001b[38;5;28;01mimport\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[34;01mrequests\u001b[39;00m\n\u001b[32m      3\u001b[39m \u001b[38;5;28;01mdef\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[34mnotify_family\u001b[39m(msg):\n\u001b[32m      4\u001b[39m     token = \u001b[33m\"\u001b[39m\u001b[33mLINE_NOTIFY_TOKEN\u001b[39m\u001b[33m\"\u001b[39m\n",
      "\u001b[31mModuleNotFoundError\u001b[39m: No module named 'requests'"
     ]
    }
   ],
   "source": [
    "import requests\n",
    "\n",
    "def notify_family(msg):\n",
    "    token = \"LINE_NOTIFY_TOKEN\"\n",
    "    headers = {\"Authorization\": f\"Bearer {token}\"}\n",
    "    data = {\"message\": msg}\n",
    "    requests.post(\"https://notify-api.line.me/api/notify\", headers=headers, data=data)\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
