import torch
import torch.nn as nn
import torch.nn.functional as F

class MultiTaskCNN(nn.Module):
    def __init__(self):
        super(MultiTaskCNN, self).__init__()
        
        ''' 
        Shared Convolutional Base
        This part of the model is shared across all tasks (gender, age, emotion).
        It extracts general features from the input images.
        '''
        self.conv_base = nn.Sequential(
            nn.Conv2d(3, 32, kernel_size=3, padding=1),  
            nn.ReLU(),                                   
            nn.MaxPool2d(kernel_size=2),                 
            nn.Conv2d(32, 64, kernel_size=3, padding=1), 
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2),
            nn.Conv2d(64, 128, kernel_size=3, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2),
            nn.Dropout(0.4),                           
            nn.Conv2d(128, 256, kernel_size=3, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2),
            nn.Dropout(0.5)
        )
        
        ''' 
        Adaptive pooling to ensure the output size is consistent regardless of the input size.
        This helps in flattening the feature maps while preserving spatial information.
        '''
        self.adaptive_pool = nn.AdaptiveAvgPool2d((4, 4))
        
        ''' 
        Task-Specific Convolutional Layers
        These layers are specific to the age and emotion tasks, respectively.
        They further process the shared features for their respective tasks.
        '''
        self.conv_age = nn.Sequential(
            nn.Conv2d(256, 128, kernel_size=3, padding=1), # Task-specific convolutional layer for age prediction
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2),
            nn.Dropout(0.4)
        )
        
        self.conv_emotion = nn.Sequential(
            nn.Conv2d(256, 128, kernel_size=3, padding=1), # Task-specific convolutional layer for emotion prediction
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2),
            nn.Dropout(0.4)
        )
        
        ''' 
        Task-Specific Fully Connected Layers
        These layers process the flattened features and make predictions for each task.
        '''
        
        # Gender prediction branch
        self.fc_gender = nn.Sequential(
            nn.Linear(256 * 4 * 4, 512),   # Fully connected layer, input size matches the output of the shared conv base
            nn.ReLU(),
            nn.Dropout(0.5),
            nn.Linear(512, 2)              # Output layer for gender classification (2 classes: Male, Female)
        )

        # Age prediction branch
        self.fc_age = nn.Sequential(
            nn.Linear(128 * 2 * 2, 1024),  # Fully connected layer, input size matches the output of task-specific conv layers for age
            nn.ReLU(),
            nn.Dropout(0.5),
            nn.Linear(1024, 512),
            nn.ReLU(),
            nn.Dropout(0.4),            
            nn.Linear(512, 8)              # Output layer for age classification (8 classes: different age groups)
        )
        
        # Emotion prediction branch
        self.fc_emotion = nn.Sequential(
            nn.Linear(128 * 2 * 2, 1024),  # Fully connected layer, input size matches the output of task-specific conv layers for emotion
            nn.ReLU(),
            nn.Dropout(0.5),
            nn.Linear(1024, 512),
            nn.ReLU(),
            nn.Dropout(0.4),
            nn.Linear(512, 8)              # Output layer for emotion classification (8 classes: different emotions)
        )
    
    def forward(self, x):
        ''' 
        Forward pass through the shared convolutional base
        '''
        x = self.conv_base(x)
        
        ''' 
        Apply adaptive pooling to obtain consistent output size
        '''
        x = self.adaptive_pool(x)
        
        ''' 
        Task-specific branches 
        '''
        
        # Gender prediction branch
        gender_features = x.view(x.size(0), -1)  # Flatten the features
        gender_out = self.fc_gender(gender_features)
        
        # Age prediction branch
        age_features = self.conv_age(x)           # Pass through task-specific conv layers for age
        age_features = age_features.view(age_features.size(0), -1)  # Flatten the features
        age_out = self.fc_age(age_features)
        
        # Emotion prediction branch
        emotion_features = self.conv_emotion(x)   # Pass through task-specific conv layers for emotion
        emotion_features = emotion_features.view(emotion_features.size(0), -1)  # Flatten the features
        emotion_out = self.fc_emotion(emotion_features)
        
        ''' 
        Return predictions for all three tasks 
        '''
        return gender_out, age_out, emotion_out
