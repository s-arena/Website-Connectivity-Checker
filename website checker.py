import requests
import win10toast
from win10toast import ToastNotifier
import time

toaster = ToastNotifier()
# The list of URLs of the websites to check
urls = ["https://youtube.com", "https://www.twitter.com", "https://www.temple.edu", "https://netflix.com", "https://www.discord.com", "https://www.hulu.com"]

# The interval (in seconds) at which to check the websites
interval = 60

while True:
  for url in urls:
    # Send a request to the website and get the response
    response = requests.get(url)

    # Check if the response was successful (i.e., the website is up)
    if response.status_code != 200:
      # Send a Windows desktop tray notification using the win10toast library
      toaster = win10toast.ToastNotifier()
      toaster.show_toast(
        "Website down",
        "The website {} is down!".format(url),
        duration=10
      )
    else:
        toaster = win10toast.ToastNotifier()
        toaster.show_toast(
        "Websites Up",
        "All Wesbites running as intended",
        duration=10
      )

  # Wait for the specified interval before checking again
  time.sleep(interval)