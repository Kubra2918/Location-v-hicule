Projet POO – Location de véhicules
Présentation

Ce projet a pour but de réaliser une application console en Python permettant de gérer une petite agence de location de véhicules.

Le programme doit permettre :

- d’afficher les clients enregistrés
- d’afficher les véhicules disponibles
- de créer une réservation
- de calculer automatiquement le coût estimé d’une location
- d’enregistrer les données dans des fichiers JSON

L’objectif principal est de mettre en pratique la programmation orientée objet et l’organisation d’un projet en plusieurs fichiers.

Description des classes
Client

La classe Client représente une personne pouvant louer un véhicule.

Elle contient les informations suivantes :

- id_client : identifiant unique du client

- nom
- prenom
- mail
- telephone
- adresse

Cette classe permet de regrouper toutes les informations liées à un client et de les afficher correctement.

Vehicule

La classe Vehicule représente un véhicule proposé à la location.

Elle contient :

- id_vehicule : identifiant unique du véhicule
- marque
- modele
- cylindree (4, 5 ou 6)
- kilometrage_actuel
- date_mise_en_circulation

Elle sert à stocker les caractéristiques d’un véhicule et à les utiliser lors d’une réservation.

Reservation

La classe Reservation correspond à une location effectuée par un client.

Elle contient :

- id_reservation
- id_client
- id_vehicule
- date_depart
- date_retour
- forfait_km
- cout_journalier
- prix_km_supp
- cout_estime

Le coût estimé est calculé automatiquement en fonction du nombre de jours de location et du tarif journalier.

TarifsManager

La classe TarifsManager gère les différents tarifs de location.

Les tarifs dépendent :

- de la cylindrée du véhicule
- du forfait kilométrique choisi

Elle contient une structure de données regroupant les tarifs ainsi que des méthodes permettant de récupérer le tarif correspondant.