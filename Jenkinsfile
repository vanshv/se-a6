pipeline { 
    agent any
    stages {
        stage('Clone Git') {
            steps {
                git 'https://github.com/vanshv/se-a6.git'
            }
        }
        stage('Send confirmation'){
            steps{
                echo 'repo cloned successfully!\ntesting started...'
            }
        }
        stage('Build Code') {
            steps {
                sh "chmod u+x sum.py"
                sh "./sum.py"
            }
        }
        stage('Test Code') {
            steps {
                sh "chmod u+x test.py"
                sh "./test.py"
            }
        }
    } 
}
