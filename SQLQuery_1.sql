
CREATE FUNCTION sum(a INT, b INT)
RETURNS INT AS $$
BEGIN

   RETURN a + b;

END; $$ LANGUAGE plpgsql;

