pipeline{
    agent any;
    stages{
        stage("code"){
            steps {
                git url:"https://github.com/Swayamnakshane/flask-app-ecs.git",branch: "main"
            }
        }
        stage("build"){
            steps {
                sh "docker build -t chatapp ."
            }
        }
        stage("push to docker"){
            steps {
                 withCredentials([usernamePassword(
                    credentialsId:"dockerhubcred",
                    passwordVariable: "dockerHubPass",
                    usernameVariable: "dockerHubUser"
                )]){
                
                sh "docker login -u ${env.dockerHubUser} -p ${env.dockerHubPass}"
                sh "docker tag chatapp ${env.dockerHubUser}/chatapp"
                sh "docker push ${env.dockerHubUser}/chatapp:latest"
                }
            }
        }
        stage("deploy"){
            steps {
                sh "docker run -itd --name escflaskapp -p 80:80 chatapp:latest"
            }
        }
    }
}
