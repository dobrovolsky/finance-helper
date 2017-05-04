--
-- PostgreSQL database dump
--

-- Dumped from database version 9.5.6
-- Dumped by pg_dump version 9.5.6

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

SET search_path = public, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: accounts; Type: TABLE; Schema: public; Owner: donnu
--

CREATE TABLE accounts (
    id integer NOT NULL,
    name character varying(30) NOT NULL,
    amount numeric NOT NULL,
    user_id integer NOT NULL
);


ALTER TABLE accounts OWNER TO donnu;

--
-- Name: accounts_id_seq; Type: SEQUENCE; Schema: public; Owner: donnu
--

CREATE SEQUENCE accounts_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE accounts_id_seq OWNER TO donnu;

--
-- Name: accounts_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: donnu
--

ALTER SEQUENCE accounts_id_seq OWNED BY accounts.id;


--
-- Name: categories; Type: TABLE; Schema: public; Owner: donnu
--

CREATE TABLE categories (
    id integer NOT NULL,
    name character varying(30) NOT NULL,
    description character varying(500),
    user_id integer NOT NULL
);


ALTER TABLE categories OWNER TO donnu;

--
-- Name: categories_id_seq; Type: SEQUENCE; Schema: public; Owner: donnu
--

CREATE SEQUENCE categories_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE categories_id_seq OWNER TO donnu;

--
-- Name: categories_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: donnu
--

ALTER SEQUENCE categories_id_seq OWNED BY categories.id;


--
-- Name: items; Type: TABLE; Schema: public; Owner: donnu
--

CREATE TABLE items (
    id integer NOT NULL,
    name character varying(30) NOT NULL,
    price numeric NOT NULL,
    count integer NOT NULL,
    description character varying(500),
    category_id integer NOT NULL,
    date date,
    user_id integer NOT NULL
);


ALTER TABLE items OWNER TO donnu;

--
-- Name: items_id_seq; Type: SEQUENCE; Schema: public; Owner: donnu
--

CREATE SEQUENCE items_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE items_id_seq OWNER TO donnu;

--
-- Name: items_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: donnu
--

ALTER SEQUENCE items_id_seq OWNED BY items.id;


--
-- Name: users; Type: TABLE; Schema: public; Owner: donnu
--

CREATE TABLE users (
    id integer NOT NULL,
    first_name character varying(30) NOT NULL,
    last_name character varying(30) NOT NULL,
    email character varying(255) NOT NULL,
    phone character varying(20)
);


ALTER TABLE users OWNER TO donnu;

--
-- Name: users_id_seq; Type: SEQUENCE; Schema: public; Owner: donnu
--

CREATE SEQUENCE users_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE users_id_seq OWNER TO donnu;

--
-- Name: users_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: donnu
--

ALTER SEQUENCE users_id_seq OWNED BY users.id;


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: donnu
--

ALTER TABLE ONLY accounts ALTER COLUMN id SET DEFAULT nextval('accounts_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: donnu
--

ALTER TABLE ONLY categories ALTER COLUMN id SET DEFAULT nextval('categories_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: donnu
--

ALTER TABLE ONLY items ALTER COLUMN id SET DEFAULT nextval('items_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: donnu
--

ALTER TABLE ONLY users ALTER COLUMN id SET DEFAULT nextval('users_id_seq'::regclass);


--
-- Data for Name: accounts; Type: TABLE DATA; Schema: public; Owner: donnu
--

INSERT INTO accounts (id, name, amount, user_id) VALUES (1, 'Cash', 1000, 1);


--
-- Name: accounts_id_seq; Type: SEQUENCE SET; Schema: public; Owner: donnu
--

SELECT pg_catalog.setval('accounts_id_seq', 1, false);


--
-- Data for Name: categories; Type: TABLE DATA; Schema: public; Owner: donnu
--

INSERT INTO categories (id, name, description, user_id) VALUES (2, 'university', '', 1);
INSERT INTO categories (id, name, description, user_id) VALUES (3, 'rest', '', 1);
INSERT INTO categories (id, name, description, user_id) VALUES (4, 'food', '', 1);
INSERT INTO categories (id, name, description, user_id) VALUES (5, 'heath', '', 1);


--
-- Name: categories_id_seq; Type: SEQUENCE SET; Schema: public; Owner: donnu
--

SELECT pg_catalog.setval('categories_id_seq', 5, true);


--
-- Data for Name: items; Type: TABLE DATA; Schema: public; Owner: donnu
--

INSERT INTO items (id, name, price, count, description, category_id, date, user_id) VALUES (5, 'bread', 4.0, 1, '', 4, '2017-05-02', 1);
INSERT INTO items (id, name, price, count, description, category_id, date, user_id) VALUES (3, 'coffee', 10.0, 12, 'i want to sleep so much!!', 2, '2017-05-02', 1);
INSERT INTO items (id, name, price, count, description, category_id, date, user_id) VALUES (6, 'water', 6.0, 2, '', 4, '2017-04-18', 1);
INSERT INTO items (id, name, price, count, description, category_id, date, user_id) VALUES (7, 'meat', 27.0, 3, '', 4, '2017-04-18', 1);
INSERT INTO items (id, name, price, count, description, category_id, date, user_id) VALUES (8, 'bicycle', 13.0, 8, '', 3, '2017-04-12', 1);
INSERT INTO items (id, name, price, count, description, category_id, date, user_id) VALUES (9, 'tea', 28.0, 1, '', 4, '2017-05-25', 1);
INSERT INTO items (id, name, price, count, description, category_id, date, user_id) VALUES (10, 'skating', 72.0, 1, '', 3, '2017-05-25', 1);
INSERT INTO items (id, name, price, count, description, category_id, date, user_id) VALUES (11, 'candy', 23.0, 2, '', 4, '2017-04-18', 1);
INSERT INTO items (id, name, price, count, description, category_id, date, user_id) VALUES (12, 'tansport', 4.0, 1, '', 2, '2017-04-20', 1);
INSERT INTO items (id, name, price, count, description, category_id, date, user_id) VALUES (13, 'potato', 16.0, 2, '', 4, '2017-04-25', 1);
INSERT INTO items (id, name, price, count, description, category_id, date, user_id) VALUES (14, 'milk', 7.0, 1, '', 2, '2017-04-18', 1);
INSERT INTO items (id, name, price, count, description, category_id, date, user_id) VALUES (15, 'meds', 13.0, 1, '', 5, '2017-05-17', 1);


--
-- Name: items_id_seq; Type: SEQUENCE SET; Schema: public; Owner: donnu
--

SELECT pg_catalog.setval('items_id_seq', 15, true);


--
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: donnu
--

INSERT INTO users (id, first_name, last_name, email, phone) VALUES (1, 'Bogdan', 'Doborovolsky', 'bogdan.gm24@gmail.com', NULL);


--
-- Name: users_id_seq; Type: SEQUENCE SET; Schema: public; Owner: donnu
--

SELECT pg_catalog.setval('users_id_seq', 1, false);


--
-- Name: accounts_pkey; Type: CONSTRAINT; Schema: public; Owner: donnu
--

ALTER TABLE ONLY accounts
    ADD CONSTRAINT accounts_pkey PRIMARY KEY (id);


--
-- Name: categories_pkey; Type: CONSTRAINT; Schema: public; Owner: donnu
--

ALTER TABLE ONLY categories
    ADD CONSTRAINT categories_pkey PRIMARY KEY (id);


--
-- Name: items_pkey; Type: CONSTRAINT; Schema: public; Owner: donnu
--

ALTER TABLE ONLY items
    ADD CONSTRAINT items_pkey PRIMARY KEY (id);


--
-- Name: users_email_key; Type: CONSTRAINT; Schema: public; Owner: donnu
--

ALTER TABLE ONLY users
    ADD CONSTRAINT users_email_key UNIQUE (email);


--
-- Name: users_pkey; Type: CONSTRAINT; Schema: public; Owner: donnu
--

ALTER TABLE ONLY users
    ADD CONSTRAINT users_pkey PRIMARY KEY (id);


--
-- Name: accounts_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: donnu
--

ALTER TABLE ONLY accounts
    ADD CONSTRAINT accounts_user_id_fkey FOREIGN KEY (user_id) REFERENCES users(id) ON UPDATE CASCADE ON DELETE RESTRICT;


--
-- Name: categories_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: donnu
--

ALTER TABLE ONLY categories
    ADD CONSTRAINT categories_user_id_fkey FOREIGN KEY (user_id) REFERENCES users(id) ON UPDATE CASCADE ON DELETE RESTRICT;


--
-- Name: items_category_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: donnu
--

ALTER TABLE ONLY items
    ADD CONSTRAINT items_category_id_fkey FOREIGN KEY (category_id) REFERENCES categories(id) ON UPDATE CASCADE ON DELETE RESTRICT;


--
-- Name: items_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: donnu
--

ALTER TABLE ONLY items
    ADD CONSTRAINT items_user_id_fkey FOREIGN KEY (user_id) REFERENCES users(id) ON UPDATE CASCADE ON DELETE RESTRICT;


--
-- Name: public; Type: ACL; Schema: -; Owner: postgres
--

REVOKE ALL ON SCHEMA public FROM PUBLIC;
REVOKE ALL ON SCHEMA public FROM postgres;
GRANT ALL ON SCHEMA public TO postgres;
GRANT ALL ON SCHEMA public TO PUBLIC;


--
-- PostgreSQL database dump complete
--

