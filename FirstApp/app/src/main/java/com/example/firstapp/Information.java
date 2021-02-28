package com.example.firstapp;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.RadioButton;
import android.widget.RadioGroup;
import android.widget.Toast;

public class Information extends AppCompatActivity
{
    RadioGroup genders;
    RadioButton gender;
    public static final String GENDER = "com.example.firstapp.GENDER";
    public static final String WEIGHT = "com.example.firstapp.WEIGHT";

    @Override
    protected void onCreate(Bundle savedInstanceState)
    {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_information);

        Button submit = (Button) findViewById(R.id.infoSubmit);

        genders = (RadioGroup) findViewById(R.id.genders);

        submit.setOnClickListener(new View.OnClickListener()
        {
            @Override
            public void onClick(View v)
            {
                submitInfo();
            }
        });



    }

    public void checkGender(View v)
    {

        Toast.makeText(this, "Selected Gender:" + gender.getText(), Toast.LENGTH_SHORT).show();
    }


    public void submitInfo()
    {
        gender = findViewById(genders.getCheckedRadioButtonId());
        String genderChosen = (String) gender.getText();

        EditText weightInput = (EditText) findViewById(R.id.weightVar);
        int weight = Integer.parseInt(weightInput.getText().toString());

        
        Intent intent = new Intent(this, MainActivity.class);
        intent.putExtra(GENDER, genderChosen);
        intent.putExtra(WEIGHT, weight);
        startActivity(intent);
    }



}