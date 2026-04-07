--
-- PostgreSQL database dump
--

\restrict Bsj75a5jFBayO4rvLMfa1438Qppj73lXufAIVB48h0KwoGaIAgLaYpfj2FpRJf2

-- Dumped from database version 18.3 (Homebrew)
-- Dumped by pg_dump version 18.3 (Homebrew)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: product; Type: TABLE; Schema: public; Owner: markomarjanovic
--

CREATE TABLE public.product (
    id integer NOT NULL,
    name character varying(100),
    description text,
    image character varying(200),
    sku integer,
    mpc double precision,
    sale_price double precision,
    stock integer,
    specs text,
    brand character varying(100),
    category character varying(100),
    active boolean DEFAULT true,
    featured boolean DEFAULT false,
    slug character varying(200),
    weight double precision,
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    updated_at timestamp without time zone
);


ALTER TABLE public.product OWNER TO markomarjanovic;

--
-- Name: product_id_seq; Type: SEQUENCE; Schema: public; Owner: markomarjanovic
--

CREATE SEQUENCE public.product_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.product_id_seq OWNER TO markomarjanovic;

--
-- Name: product_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: markomarjanovic
--

ALTER SEQUENCE public.product_id_seq OWNED BY public.product.id;


--
-- Name: product id; Type: DEFAULT; Schema: public; Owner: markomarjanovic
--

ALTER TABLE ONLY public.product ALTER COLUMN id SET DEFAULT nextval('public.product_id_seq'::regclass);


--
-- Data for Name: product; Type: TABLE DATA; Schema: public; Owner: markomarjanovic
--

COPY public.product (id, name, description, image, sku, mpc, sale_price, stock, specs, brand, category, active, featured, slug, weight, created_at, updated_at) FROM stdin;
5	Sennheiser HD380, slušalice	Sennheiser HD380 Pro su profesionalne slušalice za monitoring koje daju čisti zvuk i glasnoću do 110 dB. Slušalice su zatvorene i smanjuju zvuk do 32 dB.	slusalice-sennheiser-hd380-pro.jpg	999888775	149.99	\N	12	Boja: crna, Tip: Zatvorene, Dodatno: Profesionalni monitoring	Sennheiser	Headphones	t	t	sennheiser-hd380	0.4	2026-04-06 11:09:13.067773	\N
4	Rockcable, XLR 15m	Mikrofonski kabel, XLR (F), XLR (M); Promjer: 6mm; Dužina: 10m; Boja: crna	rockcable_15m.jpg	999888776	14.99	12	7	Boja: crna, Duljina: 15m, Dodatno: Rockcable konektor	Rockcable	Cables	t	t	rockcable-xlr-15m	0.6	2026-04-06 11:09:13.067773	2026-04-07 15:03:30.615073
6	Dynatone SLP-150 WH sa stolicom digitalni pianino	Dynatone SLP-150 je odličan početnički pianino prihvatljive cijene, kompaktnih dimenzija, bez uštede na kvaliteti. Ima odličan zvuk, svirljivost i otežanu tipku.	pianino.jpg	999888774	699	\N	2	Usb priključak, TRS out, Headphone out, 88 (NHA)tipki	Dynatone	Piano	t	f		\N	2026-04-07 14:58:46.40319	2026-04-07 15:12:38.284208
3	Klotz, XLR kabel 5m	Industrijski standard mikrofonskih kabela za glazbenike sa vrhunskom izradom i 2 Neutrik XLR konektora, 5 m dužine.\r\n\r\n	klotz_5m.jpg	999888777	32.99	\N	5	Boja: crna, Duljina: 5m, Dodatno: Neutrik konektor	Klotz	Cables	t	f	klotz-xlr-kabel-5m	0.3	2026-04-06 11:09:13.067773	2026-04-07 15:12:55.719919
\.


--
-- Name: product_id_seq; Type: SEQUENCE SET; Schema: public; Owner: markomarjanovic
--

SELECT pg_catalog.setval('public.product_id_seq', 6, true);


--
-- Name: product product_pkey; Type: CONSTRAINT; Schema: public; Owner: markomarjanovic
--

ALTER TABLE ONLY public.product
    ADD CONSTRAINT product_pkey PRIMARY KEY (id);


--
-- Name: product unique_sku; Type: CONSTRAINT; Schema: public; Owner: markomarjanovic
--

ALTER TABLE ONLY public.product
    ADD CONSTRAINT unique_sku UNIQUE (sku);


--
-- PostgreSQL database dump complete
--

\unrestrict Bsj75a5jFBayO4rvLMfa1438Qppj73lXufAIVB48h0KwoGaIAgLaYpfj2FpRJf2

