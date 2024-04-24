#chart_data = pd.DataFrame({'Nutrients': ['Proteins', 'Lipids', 'Carbs'], 'Macronutrients (g)': [protein, fats, carbs],'Details': [None, nutrients.get('FASAT').get('quantity')/servings, None]})
#chart_data.set_index('Nutrients', inplace=True)
#with st.expander("Show Nutrients"):
#st.bar_chart(data=chart_data, y=['Macronutrients (g)', 'Details'])