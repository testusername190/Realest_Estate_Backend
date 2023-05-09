// pipeline {
//     environment{
//         dockerimg = ''
//         PYTHONPATH = "/home/subham/.local/lib/python3.10/site-packages:/var/lib/jenkins/workspace/Realest_Estate_Pipeline_Django/backend"
//         DB_NAME = "realest_estate"
//         DB_HOST = "127.0.0.1"
//         DB_PORT = "3306"
//         DB_USER = "root"
//         DB_PASSWORD = "subham123"
//     }
//     agent any

//     stages {
//         stage('Git Pull') {
//             steps {
//                 git 'https://github.com/testusername190/Realest_Estate_Backend.git'
//             }
//         }
//         stage('Change Permissions and grant permission to create the log files..') {
//             steps {
//                 sh 'chmod -R 777 backend/logs'
//             }
//         }
//         stage('Install dependencies in the pipeline folder..') {
//             steps {
//                 sh 'pip install django djangorestframework django-cors-headers djangorestframework-simplejwt Pillow mysqlclient'
//             }
//         }
//         stage('Build + Test Cases') {
//             steps {
//                 echo 'Build not required for our django project, we just need to install pip in our Docker file'
//                 echo 'Test cases written for Model Testing in Django!!'
//                 sh 'cd backend/ && python3 manage.py test contacts.tests' 
//                 sh 'cd backend/ && python3 manage.py test listings.tests'
//                 sh 'cd backend/ && python3 manage.py test realtors.tests'
//             }
//         }

//         stage('Docker Build Image for Django Backend') {
//             steps {
//                 script{
//                     // sh 'cd backend/'
//                     dockerimg=docker.build("sbrc1996/realest_estate:latest")
//                 }
//             }
//         }
//         stage('Push Django Python Docker Image') {
//             steps {
//                 script{
//                     docker.withRegistry('','dockerhub'){
//                     dockerimg.push()
//                     }
//                 }
//             }
//         }
//         stage('Delete Docker Containers and Existing Images') {
//             steps {
//                 script{
//                     // here we are checking if there are any containers running in our system if so then delete them.
//                     // def running_containers = sh (returnStdout: true, script: 'docker ps -q').trim()
//                     // if (running_containers) {
//                     //     sh 'docker rm -f $(docker ps -aq)'
//                     // }
                    
//                     // sh 'docker image rm -f sbrc1996/speminiproject'
//                     sh '''
//                         # Remove all images with the tag <none>
//                         docker rmi --force $(docker images | grep "<none>" | awk '{print $3}')
//                         '''
//                 }
//             }
//         }
//         stage('Pull Frontend Docker Image from the Docker Hub')
//         {
//             steps
//             {
//                 sh 'docker pull vishalsin25/spe-major-front'
//             }
//         }
//         stage('Ansible Deploy Stage') {
//             steps {
//                 //Ansible Deploy to remote server
//                 ansiblePlaybook colorized: true, 
//                                 disableHostKeyChecking: true, 
//                                 inventory: 'inventory', 
//                                 installation:'Ansible',
//                                 playbook: 'playbook.yml', 
//                                 sudoUser: null
//             }
//         }
//     }
// }
