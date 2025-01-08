pipeline {
  agent any
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
            sh """
            cd SimpleApp/
            docker build -t ${imageName}:${imageTag} .
            """
        }
      }
    }
  }
}
