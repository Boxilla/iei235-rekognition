from datetime import datetime
import boto3

def compare_faces(sourceFile, targetFile):
    try:
        client = boto3.client('rekognition',
                    region_name='us-east-1',
                    aws_access_key_id="ASIA4GIR3VOGG2SXFHQV",
                    aws_secret_access_key="TZud83sTyGqP6akzI/sR0R+G0E2wiImraO0DTKdP",
                    aws_session_token="FwoGZXIvYXdzECoaDIIRu3PTh1WMKkI5OCLRAfYFSTVDa93F67+LqhaQtWqcpLIGj8rK0kb9irYrKQH/TPQDHM25+XooWg+u7n2E48WP73ipL8Z5/mQ4WcJmlPM/MhtmtLtXMMNLlw02C6J+1UtXluXWEKUSdWvliDjLjcZUNoyjNW73BgPGfYhNTRT4uMtKzhIHoupkjrzz0/XLdp+5EEfbsPGzAH5PxC0La0XKycqLFDSgIwJyCWKHm+VRL/gAA1Aq52Bu4yjO4TPcFYJZoHKM6yEsgvGUQ7uoFaC1cvRP5q64KEWiRwe395+oKMmOyoYGMi13LowbRzMPD7X3pK92zvs0blZ1T+zmJx7laquwT9jR5rt71qyxO5GgCCFIsQU=")
    
        imageSource=open(sourceFile,'rb')
        imageTarget=open(targetFile,'rb')

        response=client.compare_faces(SimilarityThreshold=80,
                                    SourceImage={'Bytes': imageSource.read()},
                                    TargetImage={'Bytes': imageTarget.read()})
        
        for faceMatch in response['FaceMatches']:
            position = faceMatch['Face']['BoundingBox']
            similarity = str(faceMatch['Similarity'])
            print('The face at ' +
                str(position['Left']) + ' ' +
                str(position['Top']) +
                ' matches with ' + similarity + '% confidence')
        output = ''
        if len(response['FaceMatches']) != 0:
            output = 'Luke aparece en la imagen'
        else:
            output = 'Luke no aparece en la imagen'
        logMaker(sourceFile, targetFile, output, 1)
        imageSource.close()
        imageTarget.close()
    
    except TypeError as err:
        output = "ERROR, " + str(err)
        logMaker(sourceFile, targetFile, output, 1)

    except KeyboardInterrupt as err:
        output = "ERROR, "+ str(err)
        logMaker(sourceFile, targetFile, output, 1)

    except MemoryError as err:
        output = "ERROR, " + str(err)
        logMaker(sourceFile, targetFile, output, 1)

def logMaker(img1, img2, output,  err = 0):
    ahora = datetime.now()
    date = '{ ' + '"fecha": "{}" , '.format(ahora)

    try:
        file = open('log_tarea_rekognition.txt', 'a', encoding="utf-8")
    except OSError() as err:
        log = "WARNING, " + str(err)
        print(log)
        return 0
    else:
        log = ""
        if err == 0:
            log = date + '"img1": "{}" , "img2": "{}" , "output": "{}" '.format(img1, img2, output) + ' }\n'
            log.encode('utf-8')
            file.write(log)
            file.close()
        else:
            print(output)
            log = date + '"img1": "{}" , "img2": "{}" , "output": "{}" '.format(img1, img2, output) + ' }\n'
            log.encode('utf-8')
            file.write(log)
            file.close()
            return 1       

def main():
    img_list = ['Han_solo.jpg','luke_skywalker1.jpg','luke_skywalkerAdulto1.jpg','luke_skywalkerAdulto2.jpg',
    'luke_skywalkerAdulto3.jpg','luke_skywalkerCaricatura.jpg','luke_skywalkerEdadViejo.jpg','luke_skywalkerFormatoDistinto.bmp',
    'luke_skywalkerFormatoPng.png','luke_skywalkerMismaEdad.jpg','luke_skywalkerVideoJuegoRealista.jpg',
    'luke_junto_a_actor_diferente.jpg','ValorMinimoResolucion1.jpg','ValorMinimoResolucion2.jpg','ValorMaximoResolucion1.jpg']

    stoper = ''
    while stoper != 'X' and stoper != 'x':
        target_file='.\images/skywalker_star_wars_the_mandalorian_crop1609270240914.png'
        source_file='.\images/'
        print('Imagenes disponibles:')
        counter = 0
        for i in img_list:
            print('Opción', counter, ':',  i)
            counter += 1
        img = input('Ingrese número de opción: ')
        while len(img) < 1:
            img = input('Ingrese número de opción: ')
        source_file += img_list[int(img)]
        compare_faces(source_file, target_file)
        stoper = input('ENTER para repetir, o escriba X para salir.')

    face_matches=compare_faces(source_file, target_file)
    print("Face matches: " + str(face_matches))


if __name__ == "__main__":
    main()
