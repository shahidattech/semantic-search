import React from 'react';
import { Provider } from 'react-redux';
import { configureStore, combineReducers } from '@reduxjs/toolkit';
import { persistStore, persistReducer, FLUSH, REHYDRATE, PAUSE, PERSIST, PURGE, REGISTER } from 'redux-persist'
import { PersistGate } from 'redux-persist/integration/react';
import storage from 'redux-persist/lib/storage';

export const StoreProvider = ({ children }) => {
    return (
        <Provider>
            <PersistGate loading={null}>
                {children}
            </PersistGate>
        </Provider>
    )
};