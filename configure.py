import os

class Config:
    def __init__(self):
        # project path
        self.project_path = os.path.dirname(os.path.abspath(__file__))

        # database
        self.dataset_path_db = os.path.join(self.project_path, 'offic_max.db')

        # models path
        self.model_path = os.path.join(self.project_path, 'models')
        self.main_intent_model_path = os.path.join(self.model_path, 'main_intent')
        self.main_intent_model_LSTM_path = os.path.join(self.main_intent_model_path, 'main.pt')
        self.main_intent_label_csv_path = os.path.join(self.main_intent_model_path, 'main_intent_label.tsv')
        self.main_intent_vocab_json = os.path.join(self.main_intent_model_path, 'vocab.json')
        # self.main_model_BERT_path = os.path.join(self.model_path, 'main_intent/main_intent.pt')
        self.mir_model_path = os.path.join(self.model_path, 'mir')

        # intent_recognition path
        self.predictor_path = os.path.join(self.project_path, 'services/language_service/intent_recognition')

        # Robot service
        # mir-------------------------------------------------------------------------------------
        self.MiR_host = 'http://192.168.12.20/api/v2.0.0/'
        self.headers = {'Content-Type': 'application/json', 'Accept-Language': 'en_US',
                        'Authorization': 'Basic YWRtaW46OGM2OTc2ZTViNTQxMDQxNWJkZTkwOGJkNGRlZTE1ZGZiMTY3YTljODczZmM0YmI4YTgxZjZmMmFiNDQ4YTkxOA=='}
        self.mir_path = os.path.join(self.predictor_path, 'mir')
        self.mir_dataset_path = os.path.join(self.mir_path, 'data')
        self.mir_task = 'mir'
        self.mir_intent_label = 'intent_label.txt'
        self.mir_slot_label = 'slot_label.txt'
        self.best_distance = 1.2

        self.main_intent_predictor_path = os.path.join(self.predictor_path, 'main_intent')
        # self.swarm_json = os.path.join(self.dataset_path, 'swarm/polybottest-firebase-key.json')

        # services
        self.service_list = os.path.join(self.project_path, 'services/service_list.json')
        self.required_slot = os.path.join(self.project_path, 'services/language_service/state_tracker/required_slot.json')
        self.confidence = 3.8

        # small talk
        self.api_key = "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"

        # speak to text
        self.sample_rate = 48000
        self.chunk_size = 2048
        self.hint_sound = os.path.join(self.project_path, 'hint.mp3')

        # recorder path
        self.recorder_path = os.path.join(self.project_path, 'messenger_service/recorders/')

        # text to speech
        self.voice_id = 'Matthew'
        self.voice_path = os.path.join(self.project_path, 'voice_audio/')

        # conversation json file
        self.conv_json = os.path.join(self.project_path, 'static/data/conv.json')

        # trigger words
        self.trigger_word_max = ["max", "macs"]
        self.trigger_word_mir = ["mobile robot"]
        self.trigger_word_franka = ["franka", "franca", "frankia", "frank"]
        self.trigger_word_swarm = ["swarm"]
        self.trigger_word_quit_mir = ['stop', 'back']
        self.trigger_word_small_talk = ['small talk', "have a chat"]
        self.trigger_word_quit_small_talk = ['home', 'stop']
        self.trigger_word_introduce_capability = ['introduce', 'explain']
        self.trigger_word_message_service = ['message service', 'messages services', 'messages service', 'message services', 'message', 'yes', 'sure']
        self.trigger_word_check_message = ['check', 'read', 'listen']
        self.trigger_word_send_message = ['send', 'leave', 'deliver']
        self.trigger_word_quit_message = ['home', 'stop']
        self.trigger_word_office_staff = ['simon', 'ole', 'casper', 'dimi', 'dimitris', 'cheng', 'chen', 'morten']
        self.trigger_word_office_staff_num = ['one', 'two', 'three', 'four', 'five', 'six', '1', '2', '3', '4', '5', '6']
        self.trigger_word_continue_listen = ['yes', 'sure', 'of course', 'keep']
        self.trigger_word_stop_listen = ['no', 'stop', 'not', 'later']

        # response template
        self.response_template = os.path.join(self.project_path, 'response_template/response_template.json')

        # Max client host
        # self.max_server_host = "http://172.27.15.18:5001/"
        self.max_server_host = "http://127.0.0.1:5000/"

        # robot control agent
        self.robot_control_agent_path = os.path.join(self.project_path, 'robot_control_agent')
        self.robot_service_execution_path = os.path.join(self.robot_control_agent_path, 'robot_service_execution')
        self.robot_service_management_path = os.path.join(self.robot_control_agent_path, 'robot_service_management')
        self.waiting_music_path = os.path.join(self.robot_control_agent_path, 'load.mp3')
        self.client_service_list_path = os.path.join(self.robot_service_management_path, 'service_list.json')

        #audio=====================================
        self.typing_audio_mp3 = os.path.join(self.project_path, 'static/audio/static_sounds_typing.mp3')
        self.typing_audio_script = os.path.join(self.project_path, 'static/audio/typing_audio.py')

        # LSTM Approach
        # parameters for LSTM Model
        self.embedding_dim = 100
        self.hidden_dim = 30
        self.droupout = 0.2
        self.num_class = 10
        self.batch_size = 30
        self.epochs = 30
        self.lr = 0.001
        # default sentence length
        self.input_length = 100

        # service label

        # # project path
        # self.project_path = r'D:\bot-x'
        # # voice path (change to the local where you want to save the voice)
        # self.voice_path = 'D:/voice/'
        # # voice attention
        # self.voice_attention_path = 'main/appearance/attention.mp3'
        # # main function path
        # self.main_fun_path = os.path.join(self.project_path, 'main')
        # # appearance path
        # self.appearance_path = os.path.join(self.main_fun_path, 'appearance')
        # # image path
        # self.botx_face_path = os.path.join(self.appearance_path, 'botx_face.gif')
        # self.botx_face_script_path = os.path.join(self.appearance_path, 'botx_face.py')
        # # tone path
        # self.tone_path = os.path.join(self.appearance_path, 'tone')
        # # models path
        # self.model_path = os.path.join(self.project_path, 'models')
        # # document path
        # self.docs_path = os.path.join(self.project_path, 'docs')
        # # data
        # self.dataset_path = os.path.join(self.project_path, 'data')
        # self.dataset_ATIS_path = os.path.join(self.dataset_path, 'ATIS')
        # # train_pickle_path
        # self.train_pickle_path = os.path.join(self.dataset_ATIS_path, 'atis.train.pkl')
        # # test_pickle_path
        # self.test_pickle_path = os.path.join(self.dataset_ATIS_path, 'atis.test.pkl')
        #
        # # speak to text
        # self.sample_rate = 48000
        # self.chunk_size = 2048
        # self.hint_sound = os.path.join(self.appearance_path, 'hint.mp3')
        #
        # # main/webot------------------------------------------------------------------------
        # self.webot_path = os.path.join(self.main_fun_path, 'webot')
        # self.webot_dataset_path = os.path.join(self.webot_path, 'data')
        # self.webot_model_path = os.path.join(self.webot_path, 'mir_model')
        # self.webot_task = 'webot'
        # self.webot_intent_label = 'intent_label.txt'
        # self.webot_slot_label = 'slot_label.txt'
        #
        # # main/mir---------------------------------------------------------------------------
        # self.MiR_host = 'http://192.168.12.20/api/v2.0.0/'
        # self.headers = {'Content-Type': 'application/json', 'Accept-Language': 'en_US', 'Authorization': 'Basic YWRtaW46OGM2OTc2ZTViNTQxMDQxNWJkZTkwOGJkNGRlZTE1ZGZiMTY3YTljODczZmM0YmI4YTgxZjZmMmFiNDQ4YTkxOA=='}
        # self.mir_path = os.path.join(self.main_fun_path, 'webot')
        # self.mir_dataset_path = os.path.join(self.mir_path, 'data')
        # self.mir_model_path = os.path.join(self.mir_path, 'mir_model')
        # self.mir_task = 'mir'
        # self.mir_intent_label = 'intent_label.txt'
        # self.mir_slot_label = 'slot_label.txt'
        #
        #
        #
        # # main/intent------------------------------------------------------------------------
        # self.intent_path = os.path.join(self.main_fun_path, 'intent')
        # self.intent_dataset_path = os.path.join(self.intent_path, 'data')
        # self.intent_dataset_intent_label_path = os.path.join(self.intent_dataset_path, 'main_intent_label.tsv')
        # self.intent_dataset_train_path = os.path.join(self.intent_dataset_path, 'train/main_train.tsv')
        # self.intent_model_path = os.path.join(self.intent_path, 'model/main_intent.pt')
        #
        # # main/plus/-------------------------------------------------------------------------
        # self.plus_path = os.path.join(self.main_fun_path, 'plus')
        # # main/plus/headPositionrecognition--------------------------------------------------
        # self.HPR_path = os.path.join(self.plus_path, 'HeadPositionRecognition')
        # self.HPR_script_path = os.path.join(self.HPR_path, 'predict_HPE.py')
        # self.HPR_model_path = os.path.join(self.HPR_path, 'model/shape_predictor_68_face_landmarks.dat')
        # self.HPR_json_path = os.path.join(self.HPR_path, 'head_position_data.json')
        #
        #
        #
        #
        # # NER
        # self.ner_model_path = self.project_path + '/spacy_NER/models'
        # self.ner_dataset_path = self.project_path + '/spacy_NER/data/Odoo.json'
        #
        # # # Intents
        # # self.intent_model_path = self.project_path + '/model/cnn_model.json'
        # # self.intent_weight_path = self.project_path + '/model/cnn_weights.h5'
        # # self.intent_RNN_model_path = self.project_path + '/model/rnn_model.json'
        # # self.intent_RNN_weight_path = self.project_path + '/model/rnn_weights.h5'
        # # self.intent_LSTM_model_path = self.project_path + '/model/lstm_model.json'
        # # self.intent_LSTM_weight_path = self.project_path + '/model/lstm_weights.h5'
        # # self.intent_BERT_model_path = self.project_path + '/model/bert_model.json'
        # # self.intent_BERT_weight_path = self.project_path + '/model/bert_weights.h5'
        #
        # self.bert_model_name = "wwm_uncased_L-24_H-1024_A-16"
        # self.bert_ckpt_dir = self.project_path + '/model/' + self.bert_model_name
        # self.bert_ckpt_file = self.project_path + '/model/' + self.bert_model_name + '/bert_model.ckpt'
        # self.bert_config_file = self.project_path + '/model/' + self.bert_model_name + '/bert_config.json'
        # self.vocab_file = self.project_path + '/model/' + self.bert_model_name + '/vocab.txt'
        # self.log_dir = self.project_path + '/model/log/intent_detection/'
        #
        # # sound classification
        # self.mode = mode
        # self.nfilt = 26
        # self.nfeat = 13
        # self.nfft = 512
        # self.rate = 16000
        # self.step = int(self.rate / 10)
        # self.sound_model_path = os.path.join(self.project_path + '/sound_classification/models',
        #                                      self.mode + '.model')
        # self.p_path = os.path.join(self.project_path + '/sound_classification/pickles',
        #                            self.mode + '.p')
        # self.voice_list_path = os.path.join(self.project_path + '/sound_classification/voicelist.csv')
        # self.speaker_voice_path = os.path.join(self.project_path + '/sound_classification/speakervoice')
        #
        # # Production line
        # self.lego_production_line_path = os.path.join(
        #     self.project_path + '/Odoo/LEGO_counting_machine_two/legoCountingTwo.py')
        #
        # # googlenewsvector
        # self.google_news_path = 'C:/Users/Admin/Downloads/googlenews-vectors-negative300.bin.gz'
        #
        # # cnn/rnn parameters
        # self.maxlen = 400
        # self.steps_per_epoch = 10
        # self.validation_steps = 4
        # self.embedding_dims = 300
        # self.filters = 250
        # self.kernel_size = 3
        # self.hidden_dims = 250
        # self.epochs = 10
        # self.num_class = 10
        # self.num_neurons = 50
