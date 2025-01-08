pipeline {
  agent {
    docker { image 'ubuntu:20.04' }
  }
  stages {
    stage('Test') {
      steps {
        sh 'cat /etc/os-release'
      }
    }
  }
  stage('Build Docker Image') {
    steps {
        script {
            // Define Docker image name and tag
            def imageName = 'my-docker-image'
            def imageTag = 'latest'

            // Build the Docker image
            docker.build("${imageName}:${imageTag}", '.')
         }
      }
   }
}
