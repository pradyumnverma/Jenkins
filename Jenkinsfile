pipeline {
  agent {
    docker { image 'python:3.9-slim' }
  }
  stages {
    stage('Test') {
      steps {
        sh 'python --version'
      }
    }
  }
}
