pipeline{
    agent {label 'dev'};
    stages{
        stage("code"){
            steps {
                git url:"https://github.com/Swayamnakshane/flask-app-ecs.git",branch: "main"
            }
        }
        stage("trivy scan"){
            steps {
                sh "trivy fs . -o results.jason"
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
                sh "docker run -itd --name appfla -p 80:80 chatapp:latest"
            }
        }
    }
post{
    success{
        emailext(
            subject: "Build success",
            body: "good news build is successful",
            to: 'swayamvictus1803@gmail.com'
            )
    }
    failure{
        emailext(
            subject: "Build success",
            body: "bad news build is faild",
            to: 'swayamvictus1803@gmail.com'
            )

    }
  }
}
