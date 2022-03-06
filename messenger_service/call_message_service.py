import random
import openai
from messenger_service.recording import record
from dboperation import *
from playsound import playsound
from util_tool import *
import string

def call_message(max, cfg, text, response_template):

    text = random.choice(response_template['message_service'])
    # update to the response to the db
    reply_result = res_max(cfg.dataset_path_db, 'write', text)
    max.text_to_speech_microsoft(cfg, text)

    while True:
        # waiting for operator's command...
        text = max.speech_to_text_microsoft()
        # quit the small talk service
        if any(key in text.casefold() for key in cfg.trigger_word_quit_message):
            text = random.choice(response_template['quit_message_service'])
            # update to the response to the db
            reply_result = res_max(cfg.dataset_path_db, 'write', text)
            max.text_to_speech_microsoft(cfg, text)
            break

        # if user want to leave a message
        if any(key in text.casefold() for key in cfg.trigger_word_send_message):
            # check the service status
            status_results = status(cfg.dataset_path_db, "update", "write", "no_one_care")
            if status_results == '3':
                text = random.choice(response_template['send_message_error'])
                # update to the response to the db
                reply_result = res_max(cfg.dataset_path_db, 'write', text)
                max.text_to_speech_microsoft(cfg, text)
                break

            sender = "None"
            receiver = "None"
            # get sender name
            text = random.choice(response_template['send_message_sender'])
            # update to the response to the db
            reply_result = res_max(cfg.dataset_path_db, 'write', text)
            max.text_to_speech_microsoft(cfg, text)

            while True:
                # waiting for sender's name
                text = max.speech_to_text_microsoft()
                if len(text) > 0:
                    sender = text
                    break

                text = random.choice(response_template['send_message_sender_not_understand'])
                # update to the response to the db
                reply_result = res_max(cfg.dataset_path_db, 'write', text)
                max.text_to_speech_microsoft(cfg, text)

            # get receiver name
            text = random.choice(response_template['send_message_receiver'])
            # update to the response to the db
            reply_result = res_max(cfg.dataset_path_db, 'write', text)
            max.text_to_speech_microsoft(cfg, text)

            while True:
                # waiting for receiver's name
                text = max.speech_to_text_microsoft()
                if len(text) > 0:
                    if any(key in text.casefold() for key in ['ole', 'Ole', 'one', '1']):
                        receiver = 'Ole'
                        break
                    elif any(key in text.casefold() for key in ['Simon', 'simon', 'two', '2']):
                        receiver = 'Simon'
                        break
                    elif any(key in text.casefold() for key in ['Dimitris', 'dimistris', 'dimi', 'Dimi', 'three', '3']):
                        receiver = 'Dimi'
                        break
                    elif any(key in text.casefold() for key in ['morten', 'Morten', 'four', '4']):
                        receiver = 'Morten'
                        break
                    elif any(key in text.casefold() for key in ['Casper', 'casper', 'five', '5']):
                        receiver = 'Casper'
                        break
                    elif any(key in text.casefold() for key in ['Chen', 'chen', 'Cheng', 'cheng', 'six', '6']):
                        receiver = 'Chen'
                        break
                    # else:
                    #     while True:
                    #         # text = random.choice(response_template['send_message_receiver_number'])
                    #         # update to the response to the db
                    #         reply_result = res_max(cfg.dataset_path_db, 'write', text)
                    #         # max.text_to_speech_microsoft(cfg, text)
                    #         # text = max.speech_to_text_microsoft()
                    #         if any(key in text.casefold() for key in ['one','1']):
                    #             receiver = 'Ole'
                    #             break
                    #         elif any(key in text.casefold() for key in ['two','2']):
                    #             receiver = 'Simon'
                    #             break
                    #         elif any(key in text.casefold() for key in ['three', '3']):
                    #             receiver = 'Dimi'
                    #             break
                    #         elif any(key in text.casefold() for key in ['four', '4']):
                    #             receiver = 'Morten'
                    #             break
                    #         elif any(key in text.casefold() for key in ['five', '5']):
                    #             receiver = 'Casper'
                    #             break
                    #         elif any(key in text.casefold() for key in ['six', '6']):
                    #             receiver = 'Chen'
                    #             break
                    #         else:
                    #             continue
                    #     break

                text = random.choice(response_template['send_message_receiver_number'])
                # update to the response to the db
                reply_result = res_max(cfg.dataset_path_db, 'write', text)
                max.text_to_speech_microsoft(cfg, text)

            # get message
            text = random.choice(response_template['send_message_content'])
            # update to the response to the db
            reply_result = res_max(cfg.dataset_path_db, 'write', text)
            max.text_to_speech_microsoft(cfg, text)
            record_file_path = record(cfg)

            # save the message to the DB
            operation = "add"
            id = 0
            result = save_record_to_db(cfg.dataset_path_db, id, sender, receiver, record_file_path, operation)
            # finalize
            if result == '1':
                text = random.choice(response_template['send_message_done']).replace('#receiver', receiver)
                # update to the response to the db
                reply_result = res_max(cfg.dataset_path_db, 'write', text)
                max.text_to_speech_microsoft(cfg, text)
                return
            else:
                text = random.choice(response_template['send_message_error'])
                # update to the response to the db
                reply_result = res_max(cfg.dataset_path_db, 'write', text)
                max.text_to_speech_microsoft(cfg, text)
                return


        # if user want to check the message
        if any(key in text.casefold() for key in cfg.trigger_word_check_message):
            # get the user name
            text = random.choice(response_template['read_message_verify_receiver_name'])
            # update to the response to the db
            reply_result = res_max(cfg.dataset_path_db, 'write', text)
            max.text_to_speech_microsoft(cfg, text)
            while True:
                # waiting for the first name
                text = max.speech_to_text_microsoft()
                if len(text) > 0:
                    if any(key in text.casefold() for key in ['ole', 'Ole', 'one', '1']):
                        receiver = 'Ole'
                        break
                    elif any(key in text.casefold() for key in ['Simon', 'simon', 'two', '2']):
                        receiver = 'Simon'
                        break
                    elif any(key in text.casefold() for key in ['Dimitris', 'dimistris', 'dimi', 'Dimi', 'three', '3']):
                        receiver = 'Dimi'
                        break
                    elif any(key in text.casefold() for key in ['morten', 'Morten', 'four', '4']):
                        receiver = 'Morten'
                        break
                    elif any(key in text.casefold() for key in ['Casper', 'casper', 'five', '5']):
                        receiver = 'Casper'
                        break
                    elif any(key in text.casefold() for key in ['Chen', 'chen', 'Cheng', 'cheng', 'six', '6']):
                        receiver = 'Chen'
                        break
                    # else:
                    #     while True:
                    #         # text = random.choice(response_template['read_message_verify_receiver_name_number'])
                    #         # update to the response to the db
                    #         reply_result = res_max(cfg.dataset_path_db, 'write', text)
                    #         max.text_to_speech_microsoft(cfg, text)
                    #         text = max.speech_to_text_microsoft()
                    #         if any(key in text.casefold() for key in ['one', '1']):
                    #             receiver = 'Ole'
                    #             break
                    #         elif any(key in text.casefold() for key in ['two', '2']):
                    #             receiver = 'Simon'
                    #             break
                    #         elif any(key in text.casefold() for key in ['three', '3']):
                    #             receiver = 'Dimi'
                    #             break
                    #         elif any(key in text.casefold() for key in ['four', '4']):
                    #             receiver = 'Morten'
                    #             break
                    #         elif any(key in text.casefold() for key in ['five', '5']):
                    #             receiver = 'Casper'
                    #             break
                    #         elif any(key in text.casefold() for key in ['six', '6']):
                    #             receiver = 'Chen'
                    #             break
                    #         else:
                    #             continue
                    #     break

                text = random.choice(response_template['read_message_verify_receiver_name_number'])
                # update to the response to the db
                reply_result = res_max(cfg.dataset_path_db, 'write', text)
                max.text_to_speech_microsoft(cfg, text)

            print(receiver)

            # get the user passcode
            text = random.choice(response_template['read_message_verify_receiver_password']).replace("#receiver", receiver)
            # update to the response to the db
            reply_result = res_max(cfg.dataset_path_db, 'write', text)
            max.text_to_speech_microsoft(cfg, text)
            try_times = 0
            while True:
                # waiting for the passcode name
                password = max.speech_to_text_microsoft()
                pun_string = string.punctuation
                for i in pun_string:
                    password = password.replace(i,'')
                print(password)
                if len(password) > 0:
                    auth_result = auth(cfg.dataset_path_db, receiver, password.lower())
                    if auth_result == "3":
                        text = random.choice(response_template['send_message_error'])
                        # update to the response to the db
                        reply_result = res_max(cfg.dataset_path_db, 'write', text)
                        max.text_to_speech_microsoft(cfg, text)
                        return
                    elif auth_result == '1':
                        text = random.choice(response_template['read_message_receiver_not_registered']).replace("#receiver", receiver)
                        # update to the response to the db
                        reply_result = res_max(cfg.dataset_path_db, 'write', text)
                        max.text_to_speech_microsoft(cfg, text)
                        try_times += 1
                        if try_times < 3:
                            continue
                        else:
                            text = random.choice(response_template['read_message_receiver_kick_out']).replace(
                                "#receiver", receiver)
                            # update to the response to the db
                            reply_result = res_max(cfg.dataset_path_db, 'write', text)
                            max.text_to_speech_microsoft(cfg, text)
                            return
                    else:
                        # write the status to read
                        status_results = status(cfg.dataset_path_db, "update", "read", receiver)
                        if status_results == '3':
                            text = random.choice(response_template['send_message_error'])
                            # update to the response to the db
                            reply_result = res_max(cfg.dataset_path_db, 'write', text)
                            max.text_to_speech_microsoft(cfg, text)
                            return
                        else:
                            recorder_result = read_record_from_db(cfg.dataset_path_db, receiver)
                            if recorder_result == "3":
                                text = random.choice(response_template['send_message_error'])
                                # update to the response to the db
                                reply_result = res_max(cfg.dataset_path_db, 'write', text)
                                max.text_to_speech_microsoft(cfg, text)
                                return
                            else:
                                if (len(recorder_result)) == 0:
                                    text = random.choice(response_template['read_message_receiver_no_message']).replace(
                                "#receiver", receiver)
                                    # update to the response to the db
                                    reply_result = res_max(cfg.dataset_path_db, 'write', text)
                                    max.text_to_speech_microsoft(cfg, text)
                                    return
                                else:
                                    i = 0
                                    # total number of message
                                    text = random.choice(
                                        response_template['read_message_receiver_message_sum']).replace(
                                        "#receiver", receiver).replace("#number", str(len(recorder_result)))
                                    # update to the response to the db
                                    reply_result = res_max(cfg.dataset_path_db, 'write', text)
                                    max.text_to_speech_microsoft(cfg, text)
                                    for recorder in recorder_result:
                                        # update message status
                                        result = update_record(cfg.dataset_path_db, recorder[0])
                                        if result == '3':
                                            text = random.choice(response_template['send_message_error'])
                                            # update to the response to the db
                                            reply_result = res_max(cfg.dataset_path_db, 'write', text)
                                            max.text_to_speech_microsoft(cfg, text)
                                            return
                                        else:
                                            i += 1
                                            num = make_ordinal(i)
                                            # read message
                                            text = random.choice(
                                                response_template['read_message_receiver_read_message']).replace(
                                                "#sender", recorder[1]).replace("#number", num)
                                            # update to the response to the db
                                            reply_result = res_max(cfg.dataset_path_db, 'write', text)
                                            max.text_to_speech_microsoft(cfg, text)
                                            playsound(recorder[2])
                                            # ask user if want to continue
                                            if i < len(recorder_result):
                                                text = random.choice(
                                                    response_template['read_message_receiver_continue_read_message'])
                                                # update to the response to the db
                                                reply_result = res_max(cfg.dataset_path_db, 'write', text)
                                                max.text_to_speech_microsoft(cfg, text)
                                                while True:
                                                    # waiting for the passcode name
                                                    text = max.speech_to_text_microsoft()
                                                    if len(text) > 0:
                                                        if any(key in text.casefold() for key in
                                                               cfg.trigger_word_continue_listen):
                                                            break
                                                        if any(key in text.casefold() for key in
                                                               cfg.trigger_word_stop_listen):
                                                            text = random.choice(
                                                                response_template[
                                                                    'read_message_receiver_leaving'])
                                                            # update to the response to the db
                                                            reply_result = res_max(cfg.dataset_path_db, 'write', text)
                                                            max.text_to_speech_microsoft(cfg, text)
                                                            return
                                                    else:
                                                        text = random.choice(
                                                            response_template[
                                                                'did_not_catch'])
                                                        # update to the response to the db
                                                        reply_result = res_max(cfg.dataset_path_db, 'write', text)
                                                        max.text_to_speech_microsoft(cfg, text)
                                            else:
                                                text = random.choice(
                                                    response_template[
                                                        'read_message_receiver_leaving'])
                                                # update to the response to the db
                                                reply_result = res_max(cfg.dataset_path_db, 'write', text)
                                                max.text_to_speech_microsoft(cfg, text)
                                                return
