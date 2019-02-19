/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package edu.upf.taln.asr;

import edu.cmu.sphinx.api.Configuration;
import edu.cmu.sphinx.api.SpeechResult;
import edu.cmu.sphinx.api.StreamSpeechRecognizer;
import edu.cmu.sphinx.decoder.adaptation.Stats;
import edu.cmu.sphinx.decoder.adaptation.Transform;
import edu.cmu.sphinx.result.WordResult;
import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStream;

/**
 *
 * @author u96153
 */
public class Transcriber 
{
    private Configuration configuration = null;
    public StreamSpeechRecognizer recognizer = null;
    
    public Transcriber(String lang) throws IOException
    {
        this.load_configuration(lang);
    }
    
    private void load_configuration(String lang) throws IOException 
    {
        this.configuration = new Configuration();

        if(lang.equals("en"))
        {
            this.configuration.setAcousticModelPath("resource:/edu/cmu/sphinx/models/en-us/en-us");
            this.configuration.setDictionaryPath("resource:/edu/cmu/sphinx/models/en-us/cmudict-en-us.dict");
            this.configuration.setLanguageModelPath("resource:/edu/cmu/sphinx/models/en-us/en-us.lm.bin");
        }
        else if(lang.equals("es"))
        {   String basePath = "C:\\Users\\U96153\\Documents\\NetBeansProjects\\Sphinx\\src\\main\\resources\\models\\es\\";
            this.configuration.setAcousticModelPath("file:"+basePath+"model_parameters\\voxforge_es_sphinx.cd_ptm_4000\\");
            this.configuration.setDictionaryPath("file:"+basePath+"es.dict");
            this.configuration.setLanguageModelPath("file:"+basePath+"etc\\es-20k.lm");
        }
        else
        {
            throw new UnsupportedOperationException("Not supported yet");
        }
        
        this.recognizer = new StreamSpeechRecognizer(this.configuration);

        
    }
    public String speechToText(File file) throws IOException, Exception
    {
        InputStream stream = new FileInputStream(file);
        stream.skip(44);

        this.recognizer.startRecognition(stream);
        SpeechResult result = this.recognizer.getResult();
        String transcript = "";
        while(result != null) 
        {
            transcript = transcript+" "+result.getHypothesis();
            result = this.recognizer.getResult();
        }
        recognizer.stopRecognition();
        return transcript;
    }
}
