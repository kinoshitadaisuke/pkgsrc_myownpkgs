# $NetBSD$

DISTNAME=	databricks_sdk-0.76.0
PKGNAME=	${PYPKGPREFIX}-${DISTNAME}
CATEGORIES=	devel python
MASTER_SITES=	${MASTER_SITE_PYPI:=d/databricks_sdk/}

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://pypi.org/project/databricks_sdk/
COMMENT=	Databricks SDK for Python
LICENSE=	apache-2.0

# TODO: Extract dependencies from pyproject.toml

USE_LANGUAGES=	# none
USE_TOOLS+=	gmake

.include "../../lang/python/wheel.mk"
.include "../../mk/bsd.pkg.mk"
