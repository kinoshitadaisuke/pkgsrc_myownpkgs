# $NetBSD$

DISTNAME=	proglog-0.1.12
PKGNAME=	${PYPKGPREFIX}-${DISTNAME}
CATEGORIES=	devel python
MASTER_SITES=	${MASTER_SITE_PYPI:=p/proglog/}

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://pypi.org/project/proglog/
COMMENT=	progress logging system for Python
LICENSE=	mit

# TODO: Extract dependencies from pyproject.toml

USE_LANGUAGES=	# none

TOOL_DEPENDS+=	${PYPKGPREFIX}-setuptools>=0:../../devel/py-setuptools

.include "../../lang/python/wheel.mk"
.include "../../mk/bsd.pkg.mk"
