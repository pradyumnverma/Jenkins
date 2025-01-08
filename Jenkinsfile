pipeline {
  agent {
    docker { 
        image 'docker:latest' // Use Docker as the agent
        args '--privileged -v /var/run/docker.sock:/var/run/docker.sock -v $HOME/.docker:/root/.docker' // Grant access to Docker
    }
  }
  stages {
    stage('Test') {
      steps {
        sh 'cat /etc/os-release'
      }
    }
    stage('Build Docker Image') {
      steps {
        script {
            // Define Docker image name and tag
            def imageName = 'my-docker-image'
            def imageTag = 'latest'

            // Build the Docker image
            docker.build("${imageName}:${imageTag}", './SimpleApp')
        }
      }
    }
  }
}
