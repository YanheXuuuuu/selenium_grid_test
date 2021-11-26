#linux
apt install docker-compose

#ubuntu
sudo apt-get update && sudo apt-get install docker.io -y
sudo apt install docker-compose -y

sudo -i
git clone _your_handle
#build selenium test image

cd image_2
docker build -t selenium_test:v1 . 
cd ..
docker run --name selenium_testv1 -it --rm -v $(pwd):/content selenium_test:v1

#check chromedriver --version
#check selenium/hub:version to see whether they are compatible
